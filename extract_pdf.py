import sys
from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path(r"c:\Users\rattu\Downloads\L-18\ML_Sys_Design_Jaguar.pdf")
output_path = Path(r"c:\Users\rattu\Downloads\L-18\jaguar_pdf_text.txt")
if not pdf_path.is_file():
    sys.stderr.write(f"File not found: {pdf_path}\n")
    sys.exit(1)

reader = PdfReader(str(pdf_path))
text = []
for page in reader.pages:
    txt = page.extract_text()
    if txt:
        text.append(txt)

# Write extracted text to file using UTF-8
output_path.write_text("\n".join(text), encoding="utf-8")
print(f"Extracted text written to {output_path}")
