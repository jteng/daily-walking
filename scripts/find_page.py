import pdfplumber

with pdfplumber.open("daily-walk-with-God.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text and "第1周" in text and "第4日" in text:
            print(f"Found on page index: {i} (Page {i+1})")
            break
