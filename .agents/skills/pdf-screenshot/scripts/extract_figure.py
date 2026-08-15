import os
import sys
import re
import argparse
import fitz # PyMuPDF
from PIL import Image

def find_figure_page(doc, fig_label, caption_keywords, is_table):
    """Searches the PDF pages for the figure/table caption and ranks them by match quality."""
    matching_pages = []
    
    label_pattern = re.compile(rf"\b(Figure|Fig\.|Table|Tab\.)\s*{fig_label}\b", re.IGNORECASE)
    caption_start_pattern = re.compile(rf"^\s*(Figure|Fig\.|Table|Tab\.)\s*{fig_label}\b", re.IGNORECASE)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        
        if label_pattern.search(text):
            page_best_score = 0
            for block in page.get_text("blocks"):
                block_text = block[4].strip()
                if label_pattern.search(block_text):
                    block_score = 1
                    if caption_start_pattern.match(block_text):
                        block_score += 15
                    
                    # Score keywords in block
                    kw_matches = sum(2 for kw in caption_keywords if kw.lower() in block_text.lower())
                    block_score += kw_matches
                    
                    if block_score > page_best_score:
                        page_best_score = block_score
            
            matching_pages.append((page_num, page_best_score))
            
    if not matching_pages:
        # Fallback to pure keyword search
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            score = sum(2 for kw in caption_keywords if kw.lower() in text.lower())
            if score >= 4:
                matching_pages.append((page_num, score))
                
    if not matching_pages:
        return None
        
    matching_pages.sort(key=lambda x: x[1], reverse=True)
    print(f"Found potential pages: {[(p+1, s) for p, s in matching_pages]}")
    return matching_pages[0][0]

def find_caption_rect_scored(page, label, keywords):
    """Finds the bounding box of the figure/table caption block on the page."""
    label_pattern = re.compile(rf"\b(Figure|Fig\.|Table|Tab\.)\s*{label}\b", re.IGNORECASE)
    caption_start_pattern = re.compile(rf"^\s*(Figure|Fig\.|Table|Tab\.)\s*{label}\b", re.IGNORECASE)
    matching_blocks = []
    
    for block in page.get_text("blocks"):
        block_text = block[4].strip()
        if label_pattern.search(block_text):
            block_score = 1
            if caption_start_pattern.match(block_text):
                block_score += 15
            
            score = sum(2 for kw in keywords if kw.lower() in block_text.lower())
            block_score += score
            matching_blocks.append((block, block_score))
            
    if not matching_blocks:
        return None
        
    matching_blocks.sort(key=lambda x: x[1], reverse=True)
    best_block = matching_blocks[0][0]
    return fitz.Rect(best_block[0], best_block[1], best_block[2], best_block[3])

def extract_and_crop(pdf_path, fig_label, caption_keywords, fig_caption, output_path, element_type):
    """Renders page, locates caption, clusters elements, crops, and saves."""
    doc = fitz.open(pdf_path)
    is_table = element_type.lower() == "table"
    
    page_num = find_figure_page(doc, fig_label, caption_keywords, is_table)
    if page_num is None:
        print(f"Error: Could not locate page for Figure/Table {fig_label} in {pdf_path}")
        return False
        
    print(f"Rendering page {page_num + 1}...")
    page = doc[page_num]
    
    caption_rect = find_caption_rect_scored(page, fig_label, caption_keywords)
    if not caption_rect:
        print(f"Error: Could not find caption block for Figure/Table {fig_label}")
        return False
        
    print(f"Found caption block at: {caption_rect}")
    
    # Gather drawings and images
    all_rects = []
    for img_info in page.get_images():
        xref = img_info[0]
        all_rects.extend(page.get_image_rects(xref))
        
    for d in page.get_drawings():
        r = d["rect"]
        # Pad empty rects to avoid PyMuPDF include_rect empty rect bug
        if r.y0 == r.y1:
            r = fitz.Rect(r.x0, r.y0, r.x1, r.y1 + 1.0)
        if r.x0 == r.x1:
            r = fitz.Rect(r.x0, r.y0, r.x1 + 1.0, r.y1)
        all_rects.append(r)
        
    # Filter rects based on element type
    filtered_rects = []
    if is_table:
        for r in all_rects:
            # Table elements lie below the caption
            if caption_rect.y1 - 10 <= r.y0 < caption_rect.y1 + 400:
                filtered_rects.append(r)
        filtered_rects.sort(key=lambda r: r.y0) # sort closest to caption first
    else:
        for r in all_rects:
            # Figure elements lie above the caption
            if caption_rect.y0 - 400 < r.y1 <= caption_rect.y0 + 10:
                filtered_rects.append(r)
        filtered_rects.sort(key=lambda r: r.y1, reverse=True) # sort closest to caption first
        
    # Vertical clustering algorithm
    cluster_rect = None
    if filtered_rects:
        cluster_rect = fitz.Rect(filtered_rects[0])
        max_gap = 150.0 if is_table else 40.0 # larger gap to span table rows
        
        for r in filtered_rects[1:]:
            if r.x0 >= cluster_rect.x0 and r.x1 <= cluster_rect.x1 and r.y0 >= cluster_rect.y0 and r.y1 <= cluster_rect.y1:
                continue
                
            if is_table:
                gap = r.y0 - cluster_rect.y1
            else:
                gap = cluster_rect.y0 - r.y1
                
            if gap <= max_gap:
                cluster_rect.include_rect(r)
            else:
                break
                
    # Fallback if no elements found
    if not cluster_rect:
        print("Warning: No layout elements found. Falling back to default layout bounding box.")
        page_width = page.rect.width
        if is_table:
            # Table fallback box directly below caption
            cluster_rect = fitz.Rect(40, caption_rect.y1, page_width - 40, min(page.rect.height - 40, caption_rect.y1 + 250))
        else:
            # Figure fallback box directly above caption
            cluster_rect = fitz.Rect(40, max(50, caption_rect.y0 - 250), page_width - 40, caption_rect.y0)
            
    # Add a small padding of 5 points
    padding = 5
    xmin = max(0, cluster_rect.x0 - padding)
    ymin = max(50, cluster_rect.y0 - padding)
    xmax = min(page.rect.width, cluster_rect.x1 + padding)
    ymax = min(page.rect.height, cluster_rect.y1 + padding)
    
    # Scale to pixels at Zoom = 2.0
    zoom = 2.0
    left = int(xmin * zoom)
    top = int(ymin * zoom)
    right = int(xmax * zoom)
    bottom = int(ymax * zoom)
    
    # Render the high-resolution page
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    temp_page_path = output_path + ".temp_page.png"
    pix.save(temp_page_path)
    
    # Crop and save figure
    img = Image.open(temp_page_path)
    width, height = img.size
    
    left = max(0, min(left, width - 1))
    top = max(0, min(top, height - 1))
    right = max(left + 1, min(right, width))
    bottom = max(top + 1, min(bottom, height))
    
    print(f"Cropping figure: x0={left}, y0={top}, x1={right}, y1={bottom}")
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(output_path)
    print(f"Successfully extracted to {output_path}")
    
    # Clean up temp file
    if os.path.exists(temp_page_path):
        os.remove(temp_page_path)
        
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a figure or table from a PDF locally.")
    parser.add_argument("--pdf", required=True, help="Path to the PDF file")
    parser.add_argument("--label", required=True, help="Figure/Table number (e.g. '1' or '3.6')")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords to match caption block")
    parser.add_argument("--caption", required=True, help="Full caption text")
    parser.add_argument("--output", required=True, help="Output path for cropped PNG")
    parser.add_argument("--type", default="figure", choices=["figure", "table"], help="Element type (figure or table)")
    
    args = parser.parse_args()
    
    keywords_list = [kw.strip() for kw in args.keywords.split(",")]
    
    success = extract_and_crop(
        pdf_path=args.pdf,
        fig_label=args.label,
        caption_keywords=keywords_list,
        fig_caption=args.caption,
        output_path=args.output,
        element_type=args.type
    )
    
    sys.exit(0 if success else 1)
