import json
import os

#BUG_DATA_PATH = 'data/bugs.json'

def load_bug_data():
    #Check if bug data file exists
    if os.path.exists('data/bugs.json'):
        with open('data/bugs.json', 'r') as f:
            #Load return JSON data from the file
            return json.load(f)
        #Return empty dictionary if the files does not exist
    return {}

def save_bug_data(bug_data):
    with open('data/bugs.json', "w") as f:
        #Dump the data into the file with indentation of 4 spaces
        json.dump(bug_data, f, indent=4)