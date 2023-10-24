# Program Capabilities:
#       - Compare two text files and calculate the error percent
#       - Outputs missed words

# Author: Ala Chua
# Version: 0.1
# Last Modified: 10/24/23
import os
import sys
from num2words import num2words

# TODO: add flags to specify if the file is JSON

def compare(transcript_path, captions_path):
    if os.path.exists(transcript_path):
        print("Getting " + os.path.basename(transcript_path) + " transcript file...")
    if os.path.exists(captions_path):
        print("Getting " + os.path.basename(captions_path) + " captions file...")
    with open(transcript_path, "r") as file:
    # Read the entire contents of the file into a string
        transcript = file.read()
    # remove punctuation from string, only comparing words
    transcript = transcript.replace('\'','')
    transcript = transcript.replace('\"','')
    transcript = transcript.replace(',','')
    transcript = transcript.replace('.',' ')
    transcript = transcript.replace('-', ' ')
    transcript = transcript.replace('?', ' ')
    transcript = transcript.replace('!', ' ')
    transcript = transcript.lower()
    map_t = {transcript.split()[0]: 1}
    captions = ""
    with open(captions_path, "r") as file:
    # Read the entire contents of the file into a string
        line = file.readline()
        while line:
            # {'text': 'tonight the historic case former', 'start': 1.36, 'duration': 3.88}
            # Get first property in line : {'text': 'tonight the historic case former'
            text = line.split(',')[0]
            # Get text in line:  'tonight the historic case former'
            text = text.split(':')[1]
            text = text.replace('\'','')
            text = text.replace('\"','')
            text = text.replace(',','')
            text = text.replace('.',' ')
            text = text.replace('-', ' ')
            captions += text
            line.strip()
            # print(line.strip())  # Use .strip() to remove newline characters
            line = file.readline()
    captions = captions.lower()
    # create map to store words in captions
    # set first key as first word with a value of 1
    map_c = {captions.split()[0]: 1}
    print()
    count = 0
    transcript_words = transcript.split()
    caption_words = captions.split()
    for i in range(len(transcript_words)):
        str = transcript_words[i]
        if str.isdigit():
            str = number_to_words(str)
        add_to_map(map_t, str)
    # print(map_t)
    for i in range(len(caption_words)):
        str = caption_words[i]
        if str.isdigit():
            str = number_to_words(str)
        add_to_map(map_c, str)
    # print(map_c)
    map_error = {}
    for i in range(len(map_c)):
        key_list = list(map_c.keys())
        key_1 = key_list[i]
        if (contains(map_c,map_t,key_1)):
            map_error[key_1] = map_c[key_1] - map_t[key_1]
        else:
            map_error[key_1] = -400
    # for i in range(len(map_t)):
    #     key_list = list(map_t.keys())
    #     key_1 = key_list[i]
    #     if (contains(map_t,map_c,key_1)):
    #         map_error[key_1] = map_t[key_1] - map_c[key_1]
    #     else:
    #         map_error[key_1] = -400
    print()
    print(map_error)
    calculate_error(map_error)
    # print(f"Correct words: {count}")
    # print(f"Transcript words: {len(transcript_words)}")
    # print(f"Caption words: {len(caption_words)}")

def add_to_map(map, word):
    # convert map to list of str
    str_list = list(map.keys())
    for i in range(len(str_list)):
        str = str_list[i]
        if str == word:
            # increase value of str in map by 1
            map[str] += 1
            # return after increasing count
            return
    # if word does not exist in map, add to map and set value to 1
    map[word] = 1

def calculate_error(map_err):
    # [total, wrong, error %]
    result = [0,0,0]
    words = []
    keys = list(map_err.keys())
    for i in range(len(map_err)):
        key = keys[i]
        result[0] += 1
        if map_err[key] == -400:
            words.append(key)
            result[1] += 1
    result[2] = ((result[0] - result[1])/result[0]) * 100
    print("Total: " + str(result[0]))
    print("Wrong count: " + str(result[1]))
    print("Error percent: " + str(result[2]))
    print(words)


# return list of indexes where keys match
def contains(map_1, map_2, key_1):
    key_list_2 = list(map_2.keys())
    for j in range(len(key_list_2)):
        key_2 = key_list_2[j]
        if key_2 == key_1:
            return True
    return False

def number_to_words(number):
    try:
        # Convert the number to its English word representation
        word_representation = num2words(number)

        # Capitalize the first letter and return
        return word_representation
    except ValueError as e:
        # Handle the case where the number cannot be converted
        return str(e)
    
    

# transcript_path = input("Enter file path for transcription: ")
# captions_path = input("Enter file path for captions: ")
transcript_path = sys.argv[1]
captions_path = sys.argv[2]
compare(transcript_path, captions_path)