# Python imports
import re

# Library imports
import pdb
import pandas as pd
from tabulate import tabulate
from PyPDF2 import PdfReader

class CONSTANTS:
    class SEARCH_PATTERNS:
        COMP_ID = r'Comp_ID:.'
        POLE_NM = r'Pole#'
        NJUNS = r'NJUNS#:'

class PDFScraper():
    csv_path = "C:/Users/JoseAcosta/Desktop/Scraper/Dump.csv"

    @classmethod
    def run(cls, file, export = False):
        cls.csv_reader = PdfReader(file)
        comps = cls.get_comps()
        poles = cls.get_poles()
        njuns = cls.get_njuns()

        table = {
            "CompID": comps,
            "Pole#": poles,
            "NJUNS#": njuns,
        }

        df = pd.DataFrame(table)
        print(df)

        if export:
            df.to_csv(cls.csv_file_path)

        return df

    @classmethod
    def for_each_page(cls, handle, pattern):
        page_index = 0
        results = []
        while page_index < len(cls.csv_reader.pages):
            page = cls.csv_reader.pages[page_index]
            page_pdf = page.extract_text()
            page_search_results = re.finditer(pattern, page_pdf)
            results += handle(page_pdf, page_search_results)
            page_index += 1

        return results

    @classmethod
    def get_comps(cls):
        return cls.for_each_page(
            cls.search_page_for_comps,
            CONSTANTS.SEARCH_PATTERNS.COMP_ID,
        )

    @classmethod
    def search_page_for_comps(cls, page_pdf, page_results):
        page_data = []
        for result in page_results:
            start_index = result.start()
            end_index = result.end()

            # Find the start of the line
            line_start = page_pdf.rfind('\n', 0, start_index) + 1 if page_pdf.rfind('\n', 0, start_index) != -1 else 0

            # Find the end of the line
            line_end = page_pdf.find('\n', end_index)
            if line_end == -1:
                line_end = len(page_pdf)

            # Extract the entire line
            result_line = page_pdf[line_start:line_end]
            # You have to specify what characters you want to extract
            CompID = re.sub('\D', '', result_line[15:98])
            page_data.append("'" + CompID)
        return page_data

    @classmethod
    def get_njuns(cls):
        return cls.for_each_page(
            cls.search_page_for_njuns,
            CONSTANTS.SEARCH_PATTERNS.NJUNS,
        )

    @classmethod
    def search_page_for_njuns(cls, page_pdf, page_results):
        page_data = []
        for result in page_results:
            start_index = result.start()
            end_index = result.end()

            # Find the start of the line
            line_start = page_pdf.rfind('\n', 0, start_index) + 1
            if line_start != -1:
                line_start = 0

            # Find the end of the line
            line_end = page_pdf.find('\n', end_index)
            if line_end == -1:
                line_end = len(page_pdf)

            # Extract the entire line
            result_line = page_pdf[line_start:line_end]
            # You have to specify what characters you want to extract
            result_data = re.sub('\D', '', result_line[0:15])
            page_data.append(result_data)

        return page_data

    @classmethod
    def get_poles(cls):
        return cls.for_each_page(
            cls.search_page_for_poles,
            CONSTANTS.SEARCH_PATTERNS.POLE_NM,
        )

    @classmethod
    def search_page_for_poles(cls, page_pdf, page_results):
        page_data = []
        for result in page_results:
            start_index = result.start()
            end_index = result.end()

            # Find the start of the line
            line_start = page_pdf.rfind('\n', 0, start_index) + 1 if page_pdf.rfind('\n', 0, start_index) != -1 else 0

            # Find the end of the line
            line_end = page_pdf.find('\n', end_index)
            if line_end == -1:
                line_end = len(page_pdf)

            # Extract the entire line
            result_line = page_pdf[line_start:line_end]
            # You have to specify what characters you want to extract
            RawPole = re.sub(' ','',result_line[0:23])
            if RawPole[-1].isalpha():
                polenum = re.sub('\D','',result_line[0:23])
            
            else:
                polenum = re.sub(' ','',result_line[0:23])
            page_data.append(polenum)

        return page_data