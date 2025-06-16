# Import PdfReader and PdfWriter (latest PyPDF2 v3.x)
from PyPDF2 import PdfReader, PdfWriter

# Load PDF file
reader = PdfReader("a.pdf")  # No need to open with 'rb' mode
writer = PdfWriter()

# 1. Get Total Number of Pages
num_pages = len(reader.pages)  # Total pages in PDF
print("Total Pages:", num_pages)  # Example Output: Total Pages: 5

# 2. Extract Metadata (Document Info like title, author, etc.)
metadata = reader.metadata
print("Metadata:", metadata)
# Example Output:
# Metadata: {'/Title': 'Example PDF', '/Author': 'Vaishnavi', '/Producer': 'PyPDF2'}

# 3. Extract Text from a Page
page = reader.pages[0]  # Access first page (index starts at 0)
text = page.extract_text()
print("Page 1 Text:", text.encode('utf-8', 'ignore').decode('utf-8'))
# Example Output: "This is the first page of the PDF."

# 4. Rotate a Page (clockwise)
page = reader.pages[0]
page.rotate(90)  # Rotate 90 degrees clockwise
writer.add_page(page)
text = page.extract_text()
print("Page 1 Text:", text.encode('utf-8', 'ignore').decode('utf-8'))

# 5. Add All Pages to a New PDF
for page in reader.pages:
    writer.add_page(page)

# 6. Save the modified PDF to a new file
with open("output.pdf", "wb") as f_out:
    writer.write(f_out)
# Creates a new PDF file 'output.pdf' with all pages (and rotated first page)

# 7. Split/Merge Specific Pages Example
writer2 = PdfWriter()
# Extract page 2 and 3 from original PDF and save to a new PDF
for i in [1, 2]:  # Pages 2 and 3 (index 1 and 2)
    writer2.add_page(reader.pages[i])

with open("split_output.pdf", "wb") as f_out:
    writer2.write(f_out)
# Creates 'split_output.pdf' with pages 2 & 3 only.

# 8. Add Password Protection (Encrypt PDF)
writer_encrypted = PdfWriter()
for page in reader.pages:
    writer_encrypted.add_page(page)

# Encrypt with password 'vaishnavi123'
writer_encrypted.encrypt("v123")

with open("protected_output.pdf", "wb") as f_out:
    writer_encrypted.write(f_out)
# Creates 'protected_output.pdf' which now requires 'vaishnavi123' to open.
