#!/usr/bin/env python3

import csv

infile = 'rows.csv'
output = 'subset.csv'

runs = 0

with open(infile) as f, open(output, 'w') as o:
    reader = csv.reader(f)
    writer = csv.writer(o, delimiter=',')
    for row in reader:
        if runs >= 150000:
            break
        writer.writerow(row)
        runs += 1

print('Done')

