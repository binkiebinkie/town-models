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
from datetime import datetime
import os


def getTweetThenCombine():
    from .tweetManagementQuotes import getQuoteThenDelete
    from .tweetManagementAuthors import getAuthorThenDelete

    new_quote = getQuoteThenDelete()
    new_author = getAuthorThenDelete()

    combined = new_quote + '- ' + new_author

    print('COMBINDED ', combined)
    return combined
