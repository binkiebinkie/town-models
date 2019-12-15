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
import inspirational_quotes.util as util


def getTweetThenCombineInspirationalQuotes():
    from .tweetManagementQuotes import getQuoteThenDelete
    from .tweetManagementAuthors import getAuthorThenDelete

    new_quote = getQuoteThenDelete()
    new_author = getAuthorThenDelete()

    # Quotes have newline in them so remove it
    if new_quote.endswith('\n'):
        new_quote = new_quote[:-2]
    combined = new_quote + ' - ' + new_author

    return combined


def makeABunchOfTweets():
    generatedCombinedTweets = []
    # Get tweets from file
    for x in range(util.number_of_tweets_to_generate):
        generateCombinedTweet = getTweetThenCombineInspirationalQuotes()
        generatedCombinedTweets.append(generateCombinedTweet)
    print('lenghts of the generated tweets boy is ',
          len(generatedCombinedTweets))

    if util.save_tweets_to_file == True:
        current_file_path = os.path.realpath(util.current_path_dir)
        print('current_file_path', current_file_path)
        with open((current_file_path + '/results/inspirational_quotes_gentweets.txt').replace(os.sep, '/'), "w", encoding="utf-8", errors='ignore') as out:
            # Clear file first
            # out.truncate(0)

            for tweet in generatedCombinedTweets:
                out.write(tweet)

    return generatedCombinedTweets
