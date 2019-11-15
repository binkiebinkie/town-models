# Generate teh dataset based off of the JSON
# Go through JSON list and pull out object key for athor
# and each nested quote for quotes
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.preprocessing.text import Tokenizer
print('ready')
from pathlib import Path
import os
import util
import json

dataset_file = util.dataset_file
with open(current_file_path + '/datasets/' + dataset_file, "r", encoding="utf-8") as f:
    loaded_json = json.load(f)

current_file_path = os.path.realpath('/datasets/file_management')
print('CURRENT FILE PATH ', current_file_path)
urban_dict_file_path = os.path.realpath('/datasets/urbanDictionaryWords.txt')


quotes_file = open(current_file_path + '\datasets\quotes.txt', 'wb')
authors_file = open(current_file_path + '\datasets\\authors.txt', 'wb')


for author in loaded_json:
    # Send author to file
    authors_file.write(author.encode('utf8') + "\n".encode('ascii'))
    # for each quote in author array
    for quote in loaded_json[author]:
        # send this quote to file
        # encode is because there is some funky ass chaaracters
        # in the JSON file, so strip em
        quotes_file.write(quote.encode('utf8') + "\n".encode('ascii'))

print('successfully wrote to quotes_file')
print('successfully wrote to authors_file')

quotes_file.close()
authors_file.close()
