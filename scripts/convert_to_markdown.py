import sys
import os
from pypdf import PdfReader

def convert_pdf_to_md(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found.")
        sys.exit(1)

    # Ensure the output directory exists
    os.makedirs('converted', exist_ok=True)

    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n\n"

    # Determine output filename
    base_name = os.path.basename(pdf_path)
    name_no_ext = os.path.splitext(base_name)[0]
    output_path = os.path.join('converted', f"{name_no_ext}.md")

    # Write the markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Extracted Content: {base_name}\n\n")
        f.write(text)
    
    print(f"Successfully converted {pdf_path} to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/convert_to_markdown.py <path_to_pdf>")
        sys.exit(1)
    convert_pdf_to_md(sys.argv[1])