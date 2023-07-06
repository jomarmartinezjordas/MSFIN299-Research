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
- PSEi and Company historical price acquired through using `STOCKHISTORY()` function in MS Excel

## Text Extraction and Pre-processing
The FinBERT model works on raw text being a pre-trained transformers model. The pre-processing of the text was kept at a minimal in such a way that it wont change the structure of the sentences of the text. 

- Management Discussion and Analysis or Plan of Operations were manually copied and pasted due to differences in formatting of the Form17A per company. 
- A Python code was used to extract the submission dates from the provided list of the PSE. (see code.py in _src)
- Headers and table descriptions were not included. Some of those include key words such as _`increase`_ or _`decrease`_ which may affect the analysis on the sentence level
- Footnotes and descriptions pointed by `*` are not included. 
- Some special symbols such as `•`, `▪`, and `` were also omitted
- Tables are not included as well. This is consistent with the methodology of Loughran and McDonald.
- Discussion/Review of the previous year in the MD&A were not included to avoid redundancy of analysis.
- Spelling errors as observed in the raw text were not corrected. 
- Text format differences were ignored in the text selection process
- Currency symbols and url-links were removed
- Expand contracted words

**IMPORTANT NOTE:**
- take into consideration if there are other events announcements that coincide with the announcement of the annual reports
- the MD&A can be templated which may not truly reflect the company's sentiment and in a number of cases, serves as the summary of the whole annual report. _It is a useful part of the annual report to showcase the summary of performance._ It is possible that true management sentiment resides in the portion which is not a rehashed part of the other components of the annual report. 


https://www.einfochips.com/blog/nlp-text-preprocessing/

## Company level considerations
AC
- 2019 17A was subjected into a third party software to unlock the file. No parts of the whole text were altered in the process.
 
ACEN
- 2017 Annual Report unavailable from their website given start of takeover from Phinma Energy
 
AEV
- Explanation of metrics used and its respective formulas written in terms of words were not included in the text
 
AGI
- Explanation of metrics used and its respective formulas written in terms of words were not included in the text
 
ALI
- Explanation of the composition of the business segments were omitted.
 
AP
- Explanation for the MD&A such as the one presented below was omitted as it does not contribute to the sentiment of the management
 
_The following is a discussion and analysis of the Company’s consolidated financial condition and results of operations and certain trends, risks, and uncertainties that may affect its business. The critical accounting policies section discloses certain accounting policies and management judgments that are material to the Company’s results of operations and financial condition for the periods presented in this report. The discussion and analysis of the Company’s results of operations is presented in three comparative sections: the year ended December 31, 2017 compared with the year ended December 31, 2016, the year ended December 31, 2016 compared with the year ended December 31, 2015, the year ended December 31, 2015 compared with the year ended December 31, 2014._ 
 
BPI
- Presentation of the details of BSP Circular No. 1074 was not included as it does not contribute to the sentiment of the management

CNVRG
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text
- Information on Independent Accountant and Other Related Matters portion of the MD&A was not included in the text

GLO
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text
- On page, 77 of the 2021 MD&A report, there was a typographical error commited when pertaining to Las Pinas city. This was not corrected.

_Daraga in Albay have partnered with Globe for its Automated Mobile Blaster (AMBER) services to disseminate vaccination program alerts to more people in their areas. The city governments of Cauayan in Isabela, and Las Pi√±as have also opted for AMBER to communicate their public announcements to their constituents._

GTCAP
- MD&A on GTCAP is found on item 7 instead of item 6 in the reports of the other companies selected in the study. 
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text

ICT 
- Overview of the company and description of the flow of the MD&A not included from the text.
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text
- Details of previous settled or confirmed debt financing actions/decisions not included in the text anymore. Only details related to current year were taken

JFC 
- Overview of the company and description of the flow of the MD&A not included from the text.
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text
- Details of previous settled or confirmed debt financing actions/decisions not included in the text anymore. Only details related to current year were taken

JGS
- 2020 17A was subjected into a third party software to unlock the file. No parts of the whole text were altered in the process.

MBT
- Overview of the company and description of the flow of the MD&A not included from the text.
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text

MER
- was not extracted as source file has different encryption making that inhibits copying and pasting and even running it into pdf-to-text conversion programs

RLC
- MD&A is located on item 9 of the annual report

SECB
- Overview of the company and description of the flow of the MD&A not included from the text.
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text

SMC
- Overview of the company and description of the flow of the MD&A not included from the text.
- Discussion of the changes from the adaptation of IFRS16 and PFRS9 was not included
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text
- Only the discussion on the 'Events After the Reporting Date' and 'Consent Solicitation' from the 'Other Matters' were included
- SMC did not report its lengthy discussion of risk in 2020

TEL
- Overview of the company and description of the flow of the MD&A not included from the text.
- Explanation of metrics used, the components of such metrics, and its respective formulas written in terms of words were not included in the text
- PLDT has a lengthy discussion of key risks which may have been detected as negative hence the negative sentiment score.



## Key Observations
- Despite the formal kind of report, some of lines in the text are incomplete sentences.
- Some sentences are motherhood statements like _`AIC remains committed to participating in the Philippine infrastructure space and contributing to the nation’s development.`_ and does not really contribute to the true sentiment or the current status of the business.
- BDO has the most succint and direct to the point MD&A with the least motherhood statements. 
- There were some repetition of the presentation of the key formulas used in determining ratios. This could be omitted which can lessen page count of Annual Report

