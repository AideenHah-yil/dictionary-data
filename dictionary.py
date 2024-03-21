import json

def load_dictionary(data_json):
    with open(data_json, 'r') as file:
        data = json.load(file)
        return data

def word():