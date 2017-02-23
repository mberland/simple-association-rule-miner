import sys
import csv

infilename = sys.argv[1]
infile = open(infilename,'rb')
reader = csv.DictReader(infile)
for row in reader:
    print ','.join([k for k in row if (str(row[k]) != '0' and k != 'Name')])
