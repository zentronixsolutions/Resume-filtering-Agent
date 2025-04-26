import os
import PyPDF2

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def extract_texts_from_folder(folder_path):
    extracted_texts = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(file_path)
            if text is not None:
                extracted_texts[filename] = text
            else:
                print(f"Skipping file due to error: {filename}")
    return extracted_texts


folder_path = "/content/pdfs_folder"  
pdf_texts = extract_texts_from_folder(folder_path)

for filename, text in pdf_texts.items():
    print(f"\nText from {filename}:\n{text}\n{'-'*50}")
