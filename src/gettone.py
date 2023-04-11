import pandas as pd
import os

category = ["positive", "negative", "uncertainty", "litigious", "modal_strong", "modal_weak"]
url = ["http://www3.nd.edu/~mcdonald/Data/Finance_Word_Lists/LoughranMcDonald_Positive.csv",
      "http://www3.nd.edu/~mcdonald/Data/Finance_Word_Lists/LoughranMcDonald_Negative.csv",
      "http://www3.nd.edu/~mcdonald/Data/Finance_Word_Lists/LoughranMcDonald_Uncertainty.csv",
      "http://www3.nd.edu/~mcdonald/Data/Finance_Word_Lists/LoughranMcDonald_Litigious.csv",
      "http://www3.nd.edu/~mcdonald/Data/Finance_Word_Lists/LoughranMcDonald_ModalStrong.csv",
      "http://www3.nd.edu/~mcdonald/Data/Finance_Word_Lists/LoughranMcDonald_ModalWeak.csv"]

# set the path to save the CSV files
save_path = "/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/dependencies/tone"

for i in range(len(category)):
    df = pd.read_csv(url[i], header=None, names=['>>>'])
    # set the filename to the category name with .csv extension
    filename = category[i] + '.csv'
    # combine the save path with the filename
    filepath = os.path.join(save_path, filename)
    # save the DataFrame to a CSV file with the specified filepath and no index column
    df.to_csv(filepath, index=False)
