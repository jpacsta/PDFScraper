import re
from tabulate import tabulate
from PyPDF2 import PdfReader
import csv



# Upload PDF here
reader = PdfReader("C:/Users/JoseAcosta/Desktop/T2_HUB_SE2 Work Locations/2238328 - All Work LocationsDONE.pdf")
TotalPages = len(reader.pages)
count = 1
CurrentPage = 0

# Initialize data outside the loop
data = []

while count <= TotalPages:
    page = reader.pages[CurrentPage]
    pdf = page.extract_text()

    count += 1
    CurrentPage += 1

    # These blocks are where you specify what you are searching for
    pattern_comp_id = r'Comp_ID:.'
    pattern_pole_num = r'Pole#'
    pattern_njuns = r'NJUNS#:'
    pattern_attach = r'Attach'


    # Initialize variables to store data
    CompID = "Null"
    Polenum = "NULL"
    NJUNS = "Null"


        
 # Search for NJUNS
    results_njuns = re.finditer(pattern_njuns, pdf)
    for result_search_njuns in results_njuns:
        start_index = result_search_njuns.start()
        end_index = result_search_njuns.end()

        # Find the start of the line
        line_start = pdf.rfind('\n', 0, start_index) + 1 if pdf.rfind('\n', 0, start_index) != -1 else 0

        # Find the end of the line
        line_end = pdf.find('\n', end_index)
        if line_end == -1:
            line_end = len(pdf)

        # Extract the entire line
        result_line = pdf[line_start:line_end]
        # You have to specify what characters you want to extract
        NJUNS = re.sub('\D', '', result_line[0:15])
        data.append(NJUNS)


NJUNS = data

    