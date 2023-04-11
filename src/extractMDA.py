import os
import glob
import re
import PyPDF2
import spacy

nlp = spacy.load("en_core_web_lg")

# define paths for input and output folders
input_folder = "/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/data/17a_files"
output_folder = "/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/data/17a_exports"

# iterate over all PDF files in input folder
for pdf_file in glob.glob(os.path.join(input_folder, "*.pdf")):
    # extract filename without extension
    filename = os.path.splitext(os.path.basename(pdf_file))[0]
    # open PDF file
    with open(pdf_file, "rb") as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        # find page number of the MD&A section from the table of contents
        toc_page = None
        for page in range(pdf_reader.getNumPages()):
            text = pdf_reader.getPage(page).extractText()
            if re.search(r"^\s*Table of Contents\s*$", text, re.IGNORECASE):
                toc_page = page
                break
        if toc_page is None:
            print(f"No table of contents found in {pdf_file}")
            continue
        mdna_page = None
        for page in range(toc_page, pdf_reader.getNumPages()):
            text = pdf_reader.getPage(page).extractText()
            if "Management Discussion and Analysis" in text:
                mdna_page = page
                break
        if mdna_page is None:
            print(f"No MD&A section found in {pdf_file}")
            continue
        # extract text from all pages from the MD&A section onwards
        text = ""
        for page in range(mdna_page, pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page).extractText()
        # find start and end indices of MD&A section
        start_pattern = r"Item\s+6[.\s]+Management\s+Discussion\s+and\s+Analysis"
        end_pattern = r"Item\s+7"
        start_match = re.search(start_pattern, text, flags=re.IGNORECASE)
        end_match = re.search(end_pattern, text, flags=re.IGNORECASE)
        if start_match and end_match:
            start_index = start_match.start()
            end_index = end_match.start()
            # extract MD&A section and remove line breaks and page numbers
            mdna_section = text[start_index:end_index].replace("\n", " ").replace("\x0c", "")
            mdna_section = re.sub(r"\s+\d+\s", " ", mdna_section)
            # parse sentences with spacy
            doc = nlp(mdna_section)
            sentences = [sent.text.strip() for sent in doc.sents]
            # export MD&A section to text file with same filename as PDF
            output_file = os.path.join(output_folder, f"{filename}.txt")
            with open(output_file, "w") as f:
                f.write(mdna_section)
                print(f"Exported MD&A section to {output_file}")
        else:
            print(f"No MD&A section found in {pdf_file}")
