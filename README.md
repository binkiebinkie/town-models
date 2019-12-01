# Binkie Machine Learning

## Purpose

At each twitter bot endpoint, should make around 1000 or so tweets.
Return these tweets to teh server for storage and stuff

## Flow

We want to toy with our weight using the weightCreation file until we create a weight that we can get 'consistently good' content from. To modify this file, just put a dataset in the datasets folder (contained in the model folder itself) and ensure it's referenced properly. If it's referenced properly you should be able to run the file and see training happening.

.txt is generally the dataset you will train from
.hdf5 is the model you can repopulate from.
Ensure you run the files with the terminal in the root '/models/' directory
ctrl + shift + n on file to run it. ctrl + shift + m to stop
