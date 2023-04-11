import spacy
import csv
import os

# Load the English language model in spaCy
nlp = spacy.load('en_core_web_lg')

# Specify the path to the input folder containing the text files
input_folder_path = '/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/data/17a_exports'

# Specify the path to the output folder where the CSV files will be saved
output_folder_path = '/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/data/17a_scrubbed'

# Iterate through all the files in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith('.txt'):
        # Read the text file and store the content in a variable
        with open(os.path.join(input_folder_path, filename), 'r') as file:
            text = file.read()

        # Process the text with spaCy's English model
        doc = nlp(text)

        # Create an empty list to store the sentences
        sentences = []

        # Loop through each sentence in the document
        for sentence in doc.sents:
            # Remove any leading/trailing white space and new line characters
            sentence_text = sentence.text.strip().replace('\n', ' ')
            # Append the sentence text to the list of sentences
            sentences.append(sentence_text)

        # Use the source file name to create the name of the CSV file
        csv_filename = os.path.splitext(filename)[0] + '.csv'

        # Write the list of sentences to a CSV file with the same name as the source file
        with open(os.path.join(output_folder_path, csv_filename), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Sentence'])
            for sentence in sentences:
                writer.writerow([sentence])
