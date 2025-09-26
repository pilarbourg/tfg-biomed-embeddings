import os
import re

input_folder = "/Users/pilarbourg/Desktop/TFG Basic/ExtractedText/NEGATIVE"
output_folder = "CleanText/"
os.makedirs(output_folder, exist_ok=True)

def clean_text(text: str) -> str:
    # 1. Remove non-printable / control characters
    text = re.sub(r'[^\x20-\x7E\n]', ' ', text)
gi
    # 2. Replace multiple spaces/tabs with a single space
    text = re.sub(r'[ \t]+', ' ', text)

    # 3. Normalize line breaks (collapse 3+ newlines into 2)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 4. Fix broken words split by hyphen + newline (common in PDFs)
    text = re.sub(r'-\n', '', text)

    # 5. Join lines where a sentence was split mid-way
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    # 6. Strip leading/trailing whitespace
    text = text.strip()

    return text

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        in_path = os.path.join(input_folder, filename)
        out_path = os.path.join(output_folder, filename)

        with open(in_path, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()

        cleaned = clean_text(raw_text)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"Cleaned: {filename} → {out_path}")