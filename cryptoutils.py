from operator import itemgetter
import re

# region general


def analyze_letter_frequency(text: str) -> dict:
    stripped_text = clean_non_alphabetic_characters(text)
    stripped_text_length = len(stripped_text)

    occurences = get_occurences(stripped_text)
    return get_frequencies(occurences, stripped_text_length)


def clean_non_alphabetic_characters(text: str) -> str:
    regex = re.compile('[^a-z]')

    stripped_text = text.replace(" ", "").lower()
    return regex.sub('', stripped_text)


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
    for key, value in occurences.items():
        frequencies[key] = value/text_length
    return frequencies


def get_index_of_coincidence(text: str) -> float:
    occurrences = get_occurences(text)
    number_of_occurrences = len(text)

    numerator = 0
    for key, value in occurrences.items():
        numerator += value*(value-1)

    denominator = number_of_occurrences*(number_of_occurrences-1)

    return numerator/denominator


def sort_dictionary_by_value(dictionary: dict) -> list:
    return sorted(dictionary.items(), key=itemgetter(1), reverse=True)


def separate_string_with_separator(text: str, group_number: int, separator: str) -> str:
    splitted_groups = [text[i:i+group_number]
                       for i in range(0, len(text), group_number)]
    return separator.join(splitted_groups)

# endregion

# region Baconian


def transform_to_binary_by_token(text: str, zero_token: str, one_token: str) -> str:
    return text.replace(zero_token, '0').replace(one_token, '1')

# endregion
