import streamlit as st
from PyPDF2 import PdfMerger
import os

def merge_pdfs(uploaded_files, output_name):
    merger = PdfMerger()
    try:
        for file in uploaded_files:
            merger.append(file)
        with open(output_name, 'wb') as output_file:
            merger.write(output_file)
        return output_name
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        merger.close()

# Streamlit App
st.title("PDF Merger")
st.write("Upload PDF files, reorder them, and merge them into a single file.")

# File uploader
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.write("### Uploaded Files")
    file_names = [file.name for file in uploaded_files]

    # Reordering functionality
    reordered_files = st.multiselect(
        "Reorder the files by selecting them in the desired order:",
        options=file_names,
        default=file_names
    )

    # Output file name input
    output_name = st.text_input("Enter the name for the merged PDF file (without extension):")

    if st.button("Merge PDFs"):
        if not output_name:
            st.error("Please provide a name for the merged PDF file.")
        elif len(reordered_files) != len(file_names):
            st.error("Please ensure all files are included in the order.")
        else:
            # Map reordered file names back to the uploaded files
            reordered_uploaded_files = [file for name in reordered_files for file in uploaded_files if file.name == name]
            output_file = output_name + ".pdf"
            merged_file = merge_pdfs(reordered_uploaded_files, output_file)
            if merged_file:
                st.success(f"PDFs merged successfully! Download your file below.")
                with open(merged_file, "rb") as file:
                    st.download_button(
                        label="Download Merged PDF",
                        data=file,
                        file_name=output_file,
                        mime="application/pdf"
                    )