import fitz  # PyMuPDF

def extract_text_from_pdf(file) -> str:
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text.strip()

def extract_text_from_txt(file) -> str:
    return file.read().decode("utf-8").strip()