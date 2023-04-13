import pandas as pd

read_file = pd.read_csv (r'/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/dependencies/lm_stopwords.txt')
read_file.to_csv (r'/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/dependencies/lm_stopwords.csv', index=None)