import pandas as pd
from tabulate import tabulate
import csv
from CompID import *
from PoleNumbers import *
from NJUNS import *



# Specify the CSV file
csv_file_path = "C:/Users/JoseAcosta/Desktop/Scraper/Dump.csv"

#
table ={'CompID':Comps,
    'Pole#':Poles,
    'NJUNS#':NJUNS,

    }

    
df = pd.DataFrame(table)
print(df)

#Prompts user to export to CSV
user = input("Do you want to export? y/n")

if user == "y":
    
    df.to_csv(csv_file_path)