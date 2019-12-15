import os
import csv
import ast

## CONFIG
# name of txt to pull from
list_file_name = 'RAW_recipes_col8'

new_file_name = list_file_name + '_strings'

# Now just run da file boss :) yolo

# make empty arrays to fill up with content, and create file names
lines = []

# Get CWD
current_path = os.path.dirname(os.path.realpath(__file__)) 
list_file = current_path + '/' + list_file_name + '.txt'
print('list_file',list_file)

# go through lists and save contents to list
with open(list_file, 'r') as open_file:
    for line in open_file:
        line_to_list = ast.literal_eval(line)
        for item in line_to_list:
            lines.append(item)

# Write to a new file
with open(current_path + '/' + new_file_name + '.txt',  "w") as out:
    for new_line in lines:
        out.write(new_line)
        out.write("\n")        
