import os
import re
import sys
import subprocess

PAPER_MAP = {
    "BALAN 2015": "papers/IET Communications - 2015 - Indira Balan - Analysis of carrier sense multiple access protocols for channels supporting.pdf",
    "BALAN 2017": "papers/Design and performance analysis of a MAC protocol for wireless LANs\nsupporting multipacket reception.pdf",
    "GUPTA 2022": "papers/Design and analysis of IEEE 802.11 based Full Duplex WLAN MAC protocol.pdf",
    "SUSINDER BOOK": "WIFI 7 and 8/Susinder R. Gulasckaran, Sundar G. Sankaran - WI-FI 6_ Protocol and Network (2021, Artech House) - libgen.li.pdf",
    "KHOROV 2020": "WIFI 7 and 8/Current_Status_and_Directions_of_IEEE_802.11be_the_Future_Wi-Fi_7.pdf",
    "KARAMYSHEVA 2025": "WIFI 7 and 8/A Tutorial on Wi-Fi 8: The Journey\nto Ultra High Reliability.pdf",
    "NING 2026": "WIFI 7 and 8/A_Survey_on_IEEE_802.11bn_Wi-Fi_8_Advantages_of_Ultra_High_Reliability_for_Next-Generation_Wireless_LANs.pdf"
}

def process_latex_file(filepath):
    print(f"Processing LaTeX file: {filepath}")
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return
        
    with open(filepath, "r") as f:
        content = f.read()
        
    # Pattern to match: % [INSERT FIGURE/TABLE X FROM Y - Caption] or % [PLACEHOLDER: Figure/Table X from Y - Caption]
    pattern = re.compile(r"%\s*\[(?:INSERT\s+(?:FIGURE|TABLE)|PLACEHOLDER:\s*(?:Figure|Table))\s+(\S+)\s+(?:FROM|from)\s+([^-\]]+)\s*-\s*([^\]]+)\]", re.IGNORECASE)
    
    matches = list(pattern.finditer(content))
    if not matches:
        print("No figure placeholders found in this file.")
        return
        
    print(f"Found {len(matches)} figure placeholders.")
    
    # We will replace matches from end to start to avoid index shifting
    for match in reversed(matches):
        full_tag = match.group(0)
        fig_label = match.group(1).strip()
        paper_key = match.group(2).strip()
        fig_caption = match.group(3).strip()
        
        print(f"\nProcessing placeholder: {full_tag}")
        print(f"Label: {fig_label}, Paper: {paper_key}, Caption: {fig_caption}")
        
        pdf_path = PAPER_MAP.get(paper_key.upper())
        if not pdf_path:
            # Try partial matching
            for k, p in PAPER_MAP.items():
                if paper_key.upper() in k:
                    pdf_path = p
                    break
            
        if not pdf_path:
            print(f"Warning: No PDF mapping found for paper key: {paper_key}. Skipping.")
            continue
            
        # Clean up output filename
        safe_paper_name = paper_key.lower().replace(" ", "_")
        output_filename = f"fig_{safe_paper_name}_{fig_label}.png"
        output_path = os.path.join("figures", output_filename)
        
        # Keywords for finding page
        keywords = ", ".join(fig_caption.split()[:4])
        
        print(f"Running extract_figure.py for {output_path}...")
        script_path = ".agents/skills/pdf-screenshot/scripts/extract_figure.py"
        cmd = [
            "python3", script_path,
            "--pdf", pdf_path,
            "--label", fig_label,
            "--keywords", keywords,
            "--caption", fig_caption,
            "--output", output_path
        ]
        
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Successfully extracted figure: {output_path}")
            
            # Determine if it's a table or figure
            is_table = "table" in full_tag.lower()
            env_name = "table" if is_table else "figure"
            label_prefix = "tab" if is_table else "fig"
            
            # Construct LaTeX block
            latex_block = f"""\\begin{{{env_name}}}[htbp]
    \\centering
    \\includegraphics[width=0.85\\textwidth]{{{output_path}}}
    \\caption{{{fig_caption}}}
    \\label{{{label_prefix}:{safe_paper_name}_{label_prefix}{fig_label}}}
\\end{{{env_name}}}"""
            
            # Replace the tag in the content
            start, end = match.span()
            content = content[:start] + latex_block + content[end:]
            
        except subprocess.CalledProcessError as e:
            print(f"Error running extraction command: {e}")
            print(f"Command output: {e.output}")
            print(f"Command stderr: {e.stderr}")
            print(f"Skipping replacement for {full_tag}")
            
    # Save the updated LaTeX file
    with open(filepath, "w") as f:
        f.write(content)
    print(f"\nUpdated file saved: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default to introduction.tex
        latex_file = "sections/introduction.tex"
    else:
        latex_file = sys.argv[1]
        
    process_latex_file(latex_file)
