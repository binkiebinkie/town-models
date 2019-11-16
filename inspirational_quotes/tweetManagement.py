# Go to model and generate tweets from it using generateFromModel
# Depending on length of generated tweets file
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.preprocessing.text import Tokenizer
print('ready')
import tensorflow as tf
from textgenrnn import textgenrnn
import util
from datetime import datetime
import os

from tweetManagementQuotes import first_line as first_line_quote
from tweetManagementAuthors import first_line as first_line_author

combined = first_line_quote + '/n' + first_line_author

print('first_line_quote ',first_line_quote)
print('first_line ',first_line_author)
print('COMBINDED ',combined)