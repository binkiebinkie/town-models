# Actually generate tweets

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.preprocessing.text import Tokenizer
print('ready')
import tensorflow as tf
import inspirational_quotes.util as util
from textgenrnn import textgenrnn
from datetime import datetime
import os


def generatedFromWeightQuotesFn():
    # CONFIG for this file
    # If true will just print to console
    # otherwise to file
    small_generation = util.testing_inspirational_quotes
    # Are we generating authors or quotes?
    generating_quotes = True
    model_name = util.model_name_quotes
    config_name = 'quotes'

    current_path = util.current_path_dir

    current_file_path = os.path.realpath(current_path)
    file = (current_file_path + '/config/' +
            model_name + '_weights.hdf5').replace(os.sep, '/')

    textgen = textgenrnn(
        name=((current_file_path +
               '/config/' + config_name + '/{}'.format(model_name)).replace(os.sep, '/')),
        weights_path=((current_file_path +
                       '/config/' + config_name + '/{}_weights.hdf5'.format(model_name)).replace(os.sep, '/')),
        vocab_path=((current_file_path +
                     '/config/' + config_name + '/{}_vocab.json'.format(model_name)).replace(os.sep, '/')),
        config_path=((current_file_path +
                      '/config/' + config_name + '/{}_config.json'.format(model_name)).replace(os.sep, '/'))
    )
    # SAVE GENERATED STUFF TO A FILE
    # changing the temperature schedule can result in wildly different output!
    # the higher it is the more different it is
    temperature = util.temperature
    prefix = None
    n = util.number_of_quotes_to_generate
    # size - PROD
    # max_gen_length = 100000
    # size - TEST
    max_gen_length = util.number_of_quotes_to_generate

    # FILE NAMING
    # If we want fancy datetime in name, use this code
    # timestring = datetime.now().strftime('%Y%m%d_%H%M%S')
    # gen_file = '{}_gentext_{}.txt'.format(model_name, timestring)

    # If we want the file to automatically delete then
    # create for twitter, use this code
    if small_generation == True:
        textgen.generate(n=10, temperature=temperature)
    else:
        gen_file = '{}_gentext.txt'.format(model_name)
        print('About to generate new ', model_name, ' results file')
        textgen.generate_to_file(
            current_file_path + '/results/' + gen_file, temperature=temperature, prefix=prefix, n=n, max_gen_length=max_gen_length)
        print('All generated :) YOLO LOL')
