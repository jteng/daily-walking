import pdfplumber

with pdfplumber.open("daily-walk-with-God.pdf") as pdf:
    for i in range(10, 16):
        page = pdf.pages[i]
        text = page.extract_text()
        print(f"--- Page {i} ---")
        print(text)
        print("----------------")
