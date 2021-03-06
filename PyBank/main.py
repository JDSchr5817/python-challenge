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
        dateforprofit = date[i+1]
    elif change <= loss:
        loss = change
        dateforloss = date[i+1]
    changetotal += change
    
avgprofit = changetotal/totalmonths

print("Financial Analysis")
print("------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalprofit}")
print(f"Average Change: ${avgprofit}")
print(f"Greatest Increase in Profits: {dateforprofit} ${profit}")
print(f"Greatest Decrease in Profits: {dateforloss} ${loss}")


textoutput = os.path.join("Analysis", 'financial_summary.txt')
with open (textoutput, 'w', newline='') as summary:
    write = csv.writer(summary)
    write.writerows([
        ["Financial Analysis"],
        ["------------------"],
        ["Total Months: " + str(totalmonths)],
        ["Total: $" + str(totalprofit)],
        ["Average Change: $" + str(avgprofit)],
        ["Greatest Increase in Profits: " + str(dateforprofit) + " $" + str(profit)],
        ["Greatest Decrease in Profits: " + str(dateforloss) + " $" + str(loss)],
        ])
    
    
        

