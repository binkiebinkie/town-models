import os
import csv

## CONFIG
# names of text files to combine, include .txt extension
text_files = [
    'yugiohCards_col0.txt',
    'yugiohCards_col1.txt',
    'yugiohCards_col3.txt',
]

# name of new file to combine
new_file_name = 'allYugiohCards'

# Generate off of the length of the biggest list or smallest list
# This means, if the files are different lengths 
# should we stop after the length of the biggest list? Or smallest list?
use_length_of_largest_file = False

# Now just run da file boss :) yolo





# make empty arrays to fill up with content, and create file names
lists = []
for file_name in text_files:
    lists.append([])

# Get CWD
current_path = os.path.dirname(os.path.realpath(__file__)) 

file_name_index = 0
# go through each txt file and save contents to lists
for file_name in text_files:
    with open(current_path + '/' + file_name, 'r') as f:
        for line in f:
            lists[file_name_index].append(line)
        file_name_index += 1

# choose which list is the biggest or smallest, depending on config
chosen_list = 0 # index of list to use
chosen_list_index = 0 # index of current list, will change
chosen_list_len = 0
for each_list in lists:
    if use_length_of_largest_file == True:
        if len(each_list) > chosen_list_len:
            chosen_list_len = len(each_list)
            chosen_list = chosen_list_index
        chosen_list_index += 1

    elif use_length_of_largest_file == False:
        if chosen_list_index == 0 or len(each_list) < chosen_list_len:
            chosen_list_len = len(each_list)
            chosen_list = chosen_list_index
        chosen_list_index += 1

# make a new list based off biggest (or smallest) list
# Do this to change length of generated file
new_file_list = lists[chosen_list]

# copy lists variable then remove chosen list
lists_without_chosen = lists
del lists_without_chosen[chosen_list]

# make new file then write to it, based off the length of chosen list
print(current_path + '/' + new_file_name + '.txt')
with open(current_path + '/' + new_file_name + '.txt',  "w") as out:
    lists_index = 0

    for line in new_file_list:
        out.write(line)
        
        for word_list in lists_without_chosen:
            if word_list[lists_index]:
                out.write(word_list[lists_index])

        lists_index += 1

