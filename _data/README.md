# Data Gathering and Extraction
reasons for selecting the MD&A
theoretical basis for getting the date of submission


## Data Source and Collections
### _Annual Reports_
- SEC Form 17A were downloaded from the companies' respective websites. Some companies are uploading Integrated reports which are different from the Form 17A which they submit to the SEC and PSE.
- Amended reports were not used in the analysis.  
- Some reports are locked (e.g. AC's 2019 17A) and cannot be copied and pasted and had to be subjected to other extraction methods.
- Date of submission was requested for a fee from the Philippine Stock Exchange's Librarian.

### _Stock Price Data_
- PSEi historical price manually downloaded from Marketwatch.com
- Company historical price acquired through using `STOCKHISTORY()` function in MS Excel

## Data Extraction
- Management Discussion and Analysis or Plan of Operations were manually copied and pasted due to differences in formatting of the Form17A per company. 
- A Python code was used to extract the submission dates from the provided list of the PSE. (see code.py in _src)


## Notes to the Data Extraction process
- Headers and table descriptions were not included. Some of those include key words such as _`increase`_ or _`decrease`_ which may affect the analysis on the sentence level
- Footnotes and descriptions pointed by `*` are not included. 
- Some special symbols such as `•` and `▪` were also omitted
- Tables are not included as well. This is consistent with the methodology of Loughran and McDonald.
- Discussion/Review of the previous year in the MD&A were not included to avoid redundancy of analysis.
- No spelling errors as observed in the raw text were corrected. 

## Company level considerations
AC
- 2019 17A was subjected into a third party software to unlock the file. No parts of the whole text were altered in the process.
ACEN
- 2017 Annual Report unavailable from their website given start of takeover from Phinma Energy
AEV
- Explanation of metrics used and its respective formulas written in terms of words were not included in the text
AGI
- Explanation of metrics used and its respective formulas written in terms of words were not included in the text

## Key Observations
- Despite the formal kind of report, some of lines in the text are incomplete sentences.
- Some sentences are motherhood statements like _`AIC remains committed to participating in the Philippine infrastructure space and contributing to the nation’s development.`_ and does not really contribute to the true sentiment of the current status of the business.

