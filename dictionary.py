import json

def load_dictionary(data_json):
    with open(data_json, 'r') as file:
        data = json.load(file)
        return data

def get_defination(word, dictionary):
    word = word.lower() #converts word to lowercase
    if word in dictionary:
        return dictionary[word]
    else: 
        return "Word not found"
    
    
