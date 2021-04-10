import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


def print_data(budget_data):
    
    date = str(budget_data[0])
    Profitlosses = int(budget_data[1])
    
        

