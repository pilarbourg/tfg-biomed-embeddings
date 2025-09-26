import pymupdf
import os

pdf_folder = "/Users/pilarbourg/Desktop/TFG Basic/PDFs/NEGATIVE (Type 2 Diabetes:Leucine Isoleucine Valine)"

def extract_text_from_pdf(pdf_file_path, start_page=1, end_page=None):
    text = ""
    print("Reading:", pdf_file_path)
    with pymupdf.open(pdf_file_path) as pdf:
        if end_page is None:
            end_page = pdf.page_count

        for page_num in range(start_page - 1, end_page):
            page = pdf[page_num]
            text += page.get_text() + "\n"
    return text

output_folder = "ExtractedText/"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        print("Processing:", filename)
        path = os.path.join(pdf_folder, filename)
        text = extract_text_from_pdf(path)

        output_path = os.path.join(output_folder, filename.replace(".pdf", ".txt"))
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved {output_path}")