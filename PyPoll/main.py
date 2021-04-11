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

khanvotes = 0
correyvotes = 0
livotes = 0

for i in range(1, totalvoters):
    if (3, i) = str("Khan"):
        khanvotes = khanvotes + 1
    elif (3,i) = str("Correy"):
        correyvotes = correyvotes + 1
    elif (3, i) = str("Li"):
        livotes = livotes + 1
        
        
    
        
