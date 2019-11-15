import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.preprocessing.text import Tokenizer
print('ready')
import tensorflow as tf
import util
from textgenrnn import textgenrnn
from datetime import datetime
import os

# Where do we get model from
model_name = util.model_name
current_path = util.current_path

current_file_path = os.path.realpath(current_path)
file = (current_file_path + '/config/' +
        model_name + '_weights.hdf5').replace(os.sep, '/')

textgen = textgenrnn(
    weights_path=(current_file_path +
                  '/config/{}_weights.hdf5'.format(model_name)),
    vocab_path=(current_file_path +
                '/config/{}_vocab.json'.format(model_name)),
    config_path=(current_file_path +
                 '/config/{}_config.json'.format(model_name)),
)
# SAVE GENERATED STUFF TO A FILE
# changing the temperature schedule can result in wildly different output!
# the higher it is the more different it is
temperature = util.temperature
prefix = None
n = 1
# size - PROD
# max_gen_length = 100000
# size - TEST
max_gen_length = 2000

# FILE NAMING
# If we want fancy datetime in name, use this code
# timestring = datetime.now().strftime('%Y%m%d_%H%M%S')
# gen_file = '{}_gentext_{}.txt'.format(model_name, timestring)

# If we want the file to automatically delete then
# create for twitter, use this code
gen_file = '{}_gentext.txt'.format(model_name)
print('About to generate new ', model_name, ' results file')
textgen.generate_to_file(current_file_path + '/results/' + gen_file,
                         temperature=temperature,
                         prefix=prefix,
                         n=n,
                         max_gen_length=max_gen_length)
print('All generated :) YOLO LOL')
