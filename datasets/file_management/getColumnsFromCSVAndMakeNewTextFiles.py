import os
import csv

## CONFIG
# name of CSV to pull from
csv_file_name = 'RAW_recipes'

# List of columns you wanna use
columns_to_copy = [0,8,9,10]

# Now just run da file boss :) yolo

# make empty arrays to fill up with content, and create file names
lists = []
files = []
for col in columns_to_copy:
    lists.append([])
    files.append('/' + csv_file_name + f'_col{col}.txt')

# Get CWD
current_path = os.path.dirname(os.path.realpath(__file__)) 
csv_file = current_path + '/' + csv_file_name + '.csv'
print('csv_file',csv_file)

# Save first line to array for shits n gigs
fields = []

# go through csv and save contents to lists
with open(csv_file, 'r') as ygh_file:
    csv_reader = csv.reader(ygh_file)
    fields = next(csv_reader)

    for row in csv_reader:
        colIndex = 0
        for col in columns_to_copy:
            if row[col]:
                lists[colIndex].append(row[col])
            colIndex += 1
    print(f"Toatal number of rows {csv_reader.line_num}")

print('Field gen_list_1 are:' + ', '.join(field for field in fields)) 

# go through lists and save to new files for each
writeToColIndex = 0
for col in columns_to_copy:
    with open(current_path + files[writeToColIndex],  "w") as out:
        print('writing ' + str(len(lists[writeToColIndex])) + ' lines to ' + files[writeToColIndex])
        for line in lists[writeToColIndex]:
            out.write(line)
            out.write("\n")
    writeToColIndex += 1
