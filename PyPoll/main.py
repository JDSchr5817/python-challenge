import os
import csv


csvpath = os.path.join('.', 'Resources', 'election_data.csv')

totalvotes = 0
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)

    for row in csvreader:
        
        totalvotes += 1
        
        if (row[2] == "Khan"):
            khanvotes += 1
        elif (row[2] == "Correy"):
            correyvotes += 1
        elif (row[2] == "Li"):
            livotes += 1
        else:
            otooleyvotes += 1
            
    khanpercent = khanvotes / totalvotes
    correypercent = correyvotes / totalvotes
    lipercent = livotes / totalvotes
    otooleypercent = otooleyvotes / totalvotes
    
    winner = max(khanvotes, correyvotes, livotes, otooleyvotes)

    if winner == khanvotes:
        winnername = "Khan"
    elif winner == correyvotes:
        winnername = "Correy"
    elif winner == livotes:
        winnername = "Li"
    else:
        winnername = "O'Tooley" 

print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {totalvotes}")
print(f"----------------")
print(f"Kahn: {khanpercent: .3%}({khanvotes})")
print(f"Correy: {correypercent: .3%}({correyvotes})")
print(f"Li: {lipercent: .3%}({livotes})")
print(f"O'Tooley: {otooleypercent: .3%}({otooleyvotes})")
print(f"---------------")
print(f"Winner: {winnername}")
print(f"---------------")

textoutput = os.path.join("Analysis", 'vote_summary.txt')
with open (textoutput, 'w', newline='') as summary:
    write = csv.writer(summary)
    write.writerows([
    [" Election Results"],
    ["-----------------"],
    ["Total Votes: " + str(totalvotes)],
    ["-----------------"],
    ["Khan : " + str(khanpercent) + " " + str(khanvotes)],
    ["Correy : " + str(correypercent) + " " + str(correyvotes)],
    ["Li : " + str(lipercent) + " " + str(livotes)],   
    ["O'Tooley' : " + str(otooleypercent) + " " + str(otooleyvotes)],
    ["-----------------"],
    ["Winner: " + str(winnername)],
    ["-----------------"],
    ])        




        
    
        
