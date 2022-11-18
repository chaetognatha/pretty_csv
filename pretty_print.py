#!/usr/bin/env python
import csv
import sys

def check_delimiter(line):
    """Check if the delimiter is a comma or a semicolon"""
    # create dictionary with delimiters and their count
    delimiters = {',': 0, ';': 0, '\t': 0}
    for d in delimiters:
        delimiters[d] = line.count(d)
    # take the highest value
    return max(delimiters, key=delimiters.get)


# open first arg passed to script
with open(sys.argv[1], 'r') as f:
    # read first line
    line = f.readline()
    # check delimiter
    delimiter = check_delimiter(line)
    # reset file pointer
    f.seek(0)
    # create csv reader
    reader = csv.reader(f, delimiter=delimiter)
    for i, row in enumerate(reader):
        print(f'Row {i}: ', ' | '.join(row))
        print('-' * len(f'Row {i}: ' + ' | '.join(row)))