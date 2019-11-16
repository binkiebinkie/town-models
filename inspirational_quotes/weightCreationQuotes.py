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
from datetime import datetime
from textgenrnn import textgenrnn
import tensorflow as tf


model_cfg = {
    # Does it train from nothing or from a previous file/textgenrnn?
    "new_model": True,
    # set to True if want to train a word-level model (requires more data and smaller max_length)
    'word_level': False,
    # number of LSTM cells of each layer (128/256 recommended)
    'rnn_size': 128,
    'rnn_layers': 3,   # number of LSTM layers (>=2 recommended)
    # consider text both forwards and backward, can give a training boost
    'rnn_bidirectional': False,
    # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words recommended)
    'max_length': 30,
    # maximum number of words to model; the rest will be ignored (word-level model only)
    'max_words': 10000,
}

train_cfg = {
    # set to True if each text has its own line in the source file
    'line_delimited': True,
    'num_epochs': 8,   # set higher to train the model for longer
    'gen_epochs': 1,   # generates sample text from model after given number of epochs
    # proportion of input data to train on: setting < 1.0 limits model from learning perfectly
    'train_size': 0.8,
    'dropout': 0.1,   # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    # If train__size < 1.0, test on holdout dataset; will make overall training slower
    'validation': False,
    'is_csv': False   # set to True if file is a CSV exported from Excel/BigQuery/pandas
}

# TODO: Make it so each generated line is max 140 characters

# File to train from
file_name = util.generated_dataset_file_quotes
# Path of file to train from
current_file_path = os.path.realpath(util.current_path)
file = (current_file_path + '/datasets/' +
        file_name).replace(os.sep, '/')
print('filefilefilefilefile', file)

# change to set file name of resulting trained models/texts
# For initial run, you have to remove all of the paths
model_name = util.model_name_quotes
textgen = textgenrnn(
    name=current_file_path + '/config/quotes/{}'.format(model_name),

)
# weights_path=(current_file_path +
#                   '/config/quotes/{}_weights.hdf5'.format(model_name)),
#     vocab_path=(current_file_path +
#                 '/config/quotes/{}_vocab.json'.format(model_name)),
#     config_path=(current_file_path +
#                  '/config/quotes/{}_config.json'.format(model_name)),
# Training variable
train_function = textgen.train_from_file if train_cfg[
    'line_delimited'] else textgen.train_from_largetext_file

train_function(
    file_path=file.encode('utf-8'),
    new_model=model_cfg['new_model'],
    num_epochs=train_cfg['num_epochs'],
    gen_epochs=train_cfg['gen_epochs'],
    batch_size=128,
    train_size=train_cfg['train_size'],
    dropout=train_cfg['dropout'],
    validation=train_cfg['validation'],
    is_csv=train_cfg['is_csv'],
    rnn_layers=model_cfg['rnn_layers'],
    rnn_size=model_cfg['rnn_size'],
    rnn_bidirectional=model_cfg['rnn_bidirectional'],
    max_length=model_cfg['max_length'],
    dim_embeddings=100,
    word_level=model_cfg['word_level'])
