import os
import json
import re
from sentence_transformers import SentenceTransformer

text_folder = "/Users/pilarbourg/Desktop/TFG Basic/CleanText/NEGATIVE/"
embedding_folder = "Embeddings/"
os.makedirs(embedding_folder, exist_ok=True)

model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, max_tokens=800):
    """
    Splits long text into smaller chunks so embeddings stay within a reasonable size.
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current = [], ""
    
    for s in sentences:
        if len((current + " " + s).split()) > max_tokens:
            chunks.append(current.strip())
            current = s
        else:
            current += " " + s
    if current:
        chunks.append(current.strip())
    return chunks

for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        path = os.path.join(text_folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        
        chunks = chunk_text(text)

        embeddings = model.encode(chunks, show_progress_bar=True).tolist()

        out_path = os.path.join(embedding_folder, filename.replace(".txt", ".json"))
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(embeddings, f)

        print(f"Saved embeddings for {filename} → {out_path}")