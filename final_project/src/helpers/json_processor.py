"""
1. Genenerates JSON from in-memory object
2. Writes in-memory object into JSON file
"""
import json
import os


#Export file to JSON and save it in the specified path
def export_json_file(data, file_name):
    #Create directory if not exists
    if not os.path.exists("result"):
        os.makedirs("result")

    path = "result/" + file_name
    with open(path, "w") as file:
        json.dump(data, file, indent=4)