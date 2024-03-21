import json
import difflib


def load_dictionary(data_json):
    with open(data_json, 'r') as file:
        data = json.load(file)
        return data

def suggest_word(word, dictionary):
    closest_match = difflib.get_close_matches(word, dictionary.keys(), n=1)
    if closest_match:
        return f"Did you mean '{closest_match[0]}' instead of '{word}'?"
    else:
        return "No close match found"

def get_defination(word, dictionary):
    word = word.lower() #converts word to lowercase
    if word in dictionary:
        return dictionary[word]
    else: 
        return "Word not found"
    

