import re
import csv
 
# I converted the dictionary that Kai Chen based from the Loughran and McDonald Sentiment Word Lists (https://sraf.nd.edu/textual-analysis/resources/) to be a file that will be referred
csv_filename = '/Users/jomarjordas/Documents/MSFIN299/MSFIN299-Research/dependencies/limdict.csv'

with open(csv_filename) as f:
    lmdict = csv.DictReader(f)

lmdict