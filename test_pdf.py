import fitz

pdf_path = "data/documents/GitHub_Customer_Agreement_General_Terms.pdf"

doc = fitz.open(pdf_path)

text = ""

for page in doc:
    text += page.get_text()

print("Characters:", len(text))
print(text[:1000])