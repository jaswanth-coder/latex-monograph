import os
import sys
import json
import re
import argparse
import fitz # PyMuPDF
from PIL import Image
import google.generativeai as genai

# Setup API Key
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    # Try reading from parent directory .env
    env_path = "/home/jaswanth/Programing/Latex_monographbot/.env"
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if "GEMINI_API_KEY" in line:
                    API_KEY = line.split("=")[1].strip().strip('"').strip("'")
                    break

def find_figure_page(doc, fig_label, caption_keywords):
    """Searches the PDF pages for the figure label and caption keywords."""
    matching_pages = []
    
    # Compile regex for figure search (e.g. "Figure 1" or "Fig. 1")
    label_pattern = re.compile(rf"\b(Figure|Fig\.)\s*{fig_label}\b", re.IGNORECASE)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        
        # Check for figure label
        if label_pattern.search(text):
            score = 1
            # Check for caption keywords
            for kw in caption_keywords:
                if kw.lower() in text.lower():
                    score += 2
            matching_pages.append((page_num, score))
            
    if not matching_pages:
        return None
        
    # Sort by matching score descending
    matching_pages.sort(key=lambda x: x[1], reverse=True)
    print(f"Found potential pages for Figure {fig_label}: {[(p+1, s) for p, s in matching_pages]}")
    return matching_pages[0][0]

def get_figure_bbox(image_path, fig_label, fig_caption):
    """Calls Gemini to locate the bounding box of the figure in the image."""
    if not API_KEY or API_KEY.startswith("AIzaSyAFjt5"): # detect placeholder/invalid key
        print("Warning: Gemini API Key is missing or placeholder. Skipping Gemini detection.")
        return None

    img = Image.open(image_path)
    
    prompt = f"""
Find the bounding box of the figure or diagram labeled "{fig_label}" on this page image.
The caption of the figure is: "{fig_caption}".
You must return only a JSON object containing the normalized coordinates (from 0 to 1000) for the bounding box of the figure (excluding the page numbers or text outside the figure itself, but including the figure's inner contents, drawings, axes, and its caption if it's part of the figure block, or just the figure itself).
The JSON object must have keys: 'ymin', 'xmin', 'ymax', 'xmax'.
Example output:
{{"ymin": 120, "xmin": 50, "ymax": 640, "xmax": 950}}
Do not write any markdown formatting, do not wrap the JSON in ```json code blocks, and do not write any additional explanation. Return only the raw JSON.
"""
    
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        print(f"Calling Gemini to get bounding box for {fig_label}...")
        response = model.generate_content([prompt, img])
        response_text = response.text.strip()
        
        # Strip markdown code blocks if any
        response_text = re.sub(r"^```json\s*", "", response_text)
        response_text = re.sub(r"\s*```$", "", response_text)
        
        bbox = json.loads(response_text)
        return bbox
    except Exception as e:
        print(f"Gemini detection failed or API key invalid: {e}")
        print("Falling back to local heuristic detection...")
        return None

def get_fallback_bbox(page, fig_label):
    """Fallback heuristic to find figure bbox based on caption text location."""
    # Search for "Figure X" or "Fig. X"
    rects = page.search_for(f"Figure {fig_label}")
    if not rects:
        rects = page.search_for(f"Fig. {fig_label}")
    if not rects:
        rects = page.search_for(f"figure {fig_label}")
    if not rects:
        rects = page.search_for(f"fig {fig_label}")
        
    if not rects:
        print(f"Fallback: Could not find caption text for Figure {fig_label} on page.")
        return None
        
    # Find the best rect (lowest on the page is typically the caption)
    rect = rects[-1]
    print(f"Fallback: Selected caption text rect: {rect}")
    
    page_width = page.rect.width
    page_height = page.rect.height
    
    # Figure is usually above the caption.
    # We define a bounding box in points:
    # xmin: 20 points from left margin
    # xmax: page_width - 20 points
    # ymax: rect.y1 + 15 points (include caption)
    # ymin: max(0, rect.y0 - 280 points) (approx height of typical figure + spacing)
    xmin = 20
    xmax = page_width - 20
    ymax = rect.y1 + 15
    ymin = max(50, rect.y0 - 320) # Avoid page headers
    
    # Convert to normalized coordinates (0-1000)
    bbox = {
        'ymin': int(ymin / page_height * 1000),
        'xmin': int(xmin / page_width * 1000),
        'ymax': int(ymax / page_height * 1000),
        'xmax': int(xmax / page_width * 1000)
    }
    return bbox

def extract_and_crop(pdf_path, fig_label, caption_keywords, fig_caption, output_path):
    """Renders page, gets bbox from Gemini or fallback, crops and saves."""
    doc = fitz.open(pdf_path)
    page_num = find_figure_page(doc, fig_label, caption_keywords)
    
    if page_num is None:
        print(f"Error: Could not locate page for Figure {fig_label} in {pdf_path}")
        return False
        
    print(f"Rendering page {page_num + 1}...")
    page = doc[page_num]
    
    # Try Gemini first
    zoom = 2.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    
    temp_page_path = output_path + ".temp_page.png"
    pix.save(temp_page_path)
    
    bbox = get_figure_bbox(temp_page_path, fig_label, fig_caption)
    
    if not bbox:
        print("Using fallback local heuristic for figure extraction...")
        bbox = get_fallback_bbox(page, fig_label)
        
    if not bbox:
        # Clean up temp file
        if os.path.exists(temp_page_path):
            os.remove(temp_page_path)
        return False
        
    # Crop the image using bbox
    img = Image.open(temp_page_path)
    width, height = img.size
    
    ymin, xmin, ymax, xmax = bbox['ymin'], bbox['xmin'], bbox['ymax'], bbox['xmax']
    # Convert normalized coordinates (0-1000) to actual pixels
    left = int(xmin * width / 1000)
    top = int(ymin * height / 1000)
    right = int(xmax * width / 1000)
    bottom = int(ymax * height / 1000)
    
    # Ensure coordinates are within bounds
    left = max(0, min(left, width - 1))
    top = max(0, min(top, height - 1))
    right = max(left + 1, min(right, width))
    bottom = max(top + 1, min(bottom, height))
    
    print(f"Cropping with box: {(left, top, right, bottom)}")
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(output_path)
    print(f"Successfully extracted figure and saved to {output_path}")
    
    # Clean up temp page image
    if os.path.exists(temp_page_path):
        os.remove(temp_page_path)
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a figure from a PDF as an image.")
    parser.add_argument("--pdf", required=True, help="Path to the PDF file")
    parser.add_argument("--label", required=True, help="Figure number / label (e.g. '1' or '3.8')")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords to find the figure page")
    parser.add_argument("--caption", required=True, help="Full caption of the figure for Gemini matching")
    parser.add_argument("--output", required=True, help="Output path for the cropped figure image")
    
    args = parser.parse_args()
    
    keywords_list = [kw.strip() for kw in args.keywords.split(",")]
    
    success = extract_and_crop(
        pdf_path=args.pdf,
        fig_label=args.label,
        caption_keywords=keywords_list,
        fig_caption=args.caption,
        output_path=args.output
    )
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)
