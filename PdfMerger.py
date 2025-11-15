from PyPDF2 import PdfMerger
import os
import emoji

def pdfMerge():
    merger = PdfMerger()

    # Prompt user for PDF file names and order
    print("Enter the names of the PDF files to merge (comma-separated, in the desired order):")
    print("Example: file1.pdf, file2.pdf")
    pdf_input = input("PDF files: ").strip()
    pdfs = [pdf.strip() for pdf in pdf_input.split(",")]

    # Validate that all files exist
    missing_files = [pdf for pdf in pdfs if not os.path.isfile(pdf)]
    if missing_files:
        print("Error! The following files were not found:")
        for file in missing_files:
            print(f"- {file}")
        return

    # Prompt user for output file name
    output_name = input("Enter the name for the merged PDF file (without extension): ").strip()
    if not output_name:
        print("Error! Output file name cannot be empty.")
        return

    output_file = output_name + ".pdf"

    # Merge the PDFs
    try:
        for pdf in pdfs:
            with open(pdf, 'rb') as file:
                merger.append(file)
        with open(output_file, 'wb') as output:
            merger.write(output)
        print("SUCCESS! The merged file is saved as:", output_file, emoji.emojize(":fountain_pen:"))
    except Exception as e:
        print("An error occurred while merging PDFs:", str(e))
    finally:
        merger.close()

    print("Goodbye! Come again", emoji.emojize(":handshake:"))

if __name__ == "__main__":
    pdfMerge()