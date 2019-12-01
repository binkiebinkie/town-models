# Input a file you want to combine with Urban Dictionary dataset
# Along with how often you want it to use a raunchy word

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.preprocessing.text import Tokenizer
print('ready')
from pathlib import Path
import os
import json
import random

current_file_path = os.path.realpath('models/datasets/')
print('CURRENT FILE PATH ', current_file_path)

# CONFIG
# File you wanna combine with urban dictionary
other_file = current_file_path + '/fullBabyNamesData.txt'
with open(other_file, "r", encoding="utf-8") as other_opened_file_f:
    other_file_lines = other_opened_file_f.readlines()
# How often you want urban dictionary to show up
# MUST BE NEGATIVE
urban_occurance = -4
# The name of the file you are generating
new_file = current_file_path + '/urbanBabies.txt'

urban_dictionary_file = current_file_path + '/urbanDictionaryWords.txt'
with open(urban_dictionary_file, "r", encoding="utf-8") as ud_opened_f:
    urban_dictionary_lines = ud_opened_f.readlines()
# Open file were making (if it doesn't exist create it)
new_file_opened = open(new_file, "w+", encoding="utf-8")

for i in range(len(other_file_lines)):
    if i % urban_occurance == 0:
        random_urban_line = random.choice(list(urban_dictionary_lines))
        new_file_opened.write(random_urban_line)
    new_file_opened.write(other_file_lines[i])

new_file_opened.close()
