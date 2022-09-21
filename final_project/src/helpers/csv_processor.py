"""
1. Read CSV files and returns in-memory object
"""
import csv
import os
import json

#Read csv from a file until empty line and separate by tab
def get_csv_data(file_path):
    csv_data = []
    with open(file_path,'rt', encoding='utf-16') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        #Read csv until an empty line
        for row in csvreader:
            if row:
                csv_data.append(row)
            else:
                break
                
    return csv_data
    
#Read csv from one folder containing three folders every folder containing x files
def get_csv_data_as_dict(file_path):
    csv_data = {}
    for root, dirs, files in os.walk(file_path):
        for dir in dirs:
            for root, dirs, files in os.walk(file_path + "/" + dir):
                for file in files:
                    csv_data[dir +' - '+ file] = get_csv_data(file_path + "/" + dir + "/" + file)
    return results(csv_data)

def results(csv_data):
    temp = []
    results = {}
    for key, value in csv_data.items():
        #if value  not in results then 
        if value not in temp:
            temp.append(value)
            results[key] = value

    return results
    