from operator import itemgetter
import re

def analyze_letter_frequency(text: str) -> dict:
    stripped_text = clean_non_alphabetic_characters(text)
    stripped_text_length = len(stripped_text)

    occurences = get_occurences(stripped_text)
    return get_frequencies(occurences,stripped_text_length)

def clean_non_alphabetic_characters(text:str) -> str:
    regex = re.compile('[^a-z]')

    stripped_text = text.replace(" ", "").lower()
    return regex.sub('',stripped_text)

def get_occurences(text: str) -> dict:
    occurences = {}
    for letter in text:
        if letter in occurences:
            occurences[letter] = occurences[letter]+1
        else:
            occurences[letter] = 1
    return occurences


def get_frequencies(occurences: dict, text_length: int) -> dict:
    frequencies = {}
    for key,value in occurences.items():
        frequencies[key] = value/text_length
    return frequencies

def sort_dictionary_by_value(dictionary:dict) -> list:
    return sorted(dictionary.items(),key=itemgetter(1),reverse=True)
