import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


date = []
profitlosses = []

avgprofitlosses = 0
with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in csvReader:
        date.append(row[0])
        profitlosses.append(int(row[1]))
        
totalmonths = len(date)
totalprofit = sum(profitlosses)

changetotal = 0
profit = (profitlosses[1])-(profitlosses[0])
loss = (profitlosses[1])-(profitlosses[0])

for i in range(0,totalmonths-1):
    change = (profitlosses[i+1])-(profitlosses[i])
    if change >= profit:
        profit = change
        dateforprofit = dates[i+1]
    elif
    
    
        

