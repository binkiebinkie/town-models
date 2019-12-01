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
import baby_names.util as util
from datetime import datetime
import os


def getBabyName():
    from .tweetManagementBabyNames import getBabyNameThenDelete
    baby_name = getBabyNameThenDelete()
    return baby_name


def makeOneHundredTweetsBabyNames():
    generatedTweets = []
    for x in range(100):
        generateTweet = getBabyName()
        generatedTweets.append(generateTweet)
    print('lenghts of the generated one hundred ', model_name, ' boy is ',
          len(generatedTweets))
    return generatedTweets
