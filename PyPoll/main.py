import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

voterid = []
county = []
candidate = []

with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvReader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

totalvoters=len(voterid)
print(totalvoters)
