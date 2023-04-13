import os
import PyPDF2

# Specify the path of the folder containing the PDF files
folder_path = '/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/data/17a_files'

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a PDF file
    if file_name.endswith('.pdf'):
        # Create the full file path
        file_path = os.path.join(folder_path, file_name)

        # Open the PDF file in read-binary mode
        pdf_file = open(file_path, 'rb')

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Get the total number of pages in the PDF file
        num_pages = pdf_reader.numPages

        # Create an empty string to store the text
        text = ""

        # Loop through each page and extract the text
        for page in range(num_pages):
            # Get the current page object
            pdf_page = pdf_reader.getPage(page)

            # Extract the text from the page
            page_text = pdf_page.extractText()

            # Append the text to the overall string
            text += page_text

        # Close the PDF file
        pdf_file.close()

        # Find the page of the table of contents
        toc_page = None
        if "Table of Contents" in text:
            toc_page_index = text.index("Table of Contents")
            # Convert the index to the corresponding page number
            toc_page = pdf_reader.getPageNumber(pdf_reader.getPage(toc_page_index).pdf)
            print("Table of contents found in file", file_name, "on page", toc_page + 1)
        else:
            print("Table of contents not found in file", file_name)

        # Print the page containing the table of contents
        if toc_page is not None:
            pdf_page = pdf_reader.getPage(toc_page - 1)
            print(pdf_page.extractText())
