import os
from pypdf import PdfReader, PdfWriter

folder = "pdfs"
writer = PdfWriter()

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        reader = PdfReader(os.path.join(folder, file))

        for page in reader.pages:
            writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)