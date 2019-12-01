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
import inspirational_quotes.util as util
from datetime import datetime
import os


def getQuoteThenDelete():
    # Where do we get the results file from
    model_name = util.model_name_quotes
    current_path = util.current_path
    current_file_path = os.path.realpath(current_path)
    file = (current_file_path + '/results/' +
            model_name + '_gentext.txt').replace(os.sep, '/')

    # Go to file and check the number of lines from the file
    num_lines = sum(1 for line in open(file))

    # If the number of lines left is less than 10
    if num_lines < 10:
        print('There are less than 10 inspirational quotes left in txt file. Generating new quotes.')
        import inspirational_quotes.generateFromWeightQuotes
        print('New Number of quotes in results', sum(1 for line in open(file)))

    # If it's over 10 results
    # Get the first line
    # then delete it!
    with open(file, 'r') as fin:
        first_line_quotes = fin.readline()
        data = fin.read().splitlines(True)

    with open(file, 'w') as fout:
        fout.writelines(data[0:])

    # print('New number of lines left in the results file: ',
    #       sum(1 for line in open(file)))

    return first_line_quotes
