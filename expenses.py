

import os
""" Create a program called expenses.py that reads a file containing a 
list of expenses and calculates the total expense. """


# The first column is expenses typ and the second coulmn is expenses amount.
content_expenses = '''Electricity 120.50
Groceries 45.78
Entertainment 60.00
Transport 35.25
Dining 75.90
'''


with open('expenses.txt', 'w') as file:
    file.write(content_expenses)

total_cost = 0

with open('expenses.txt', 'r') as f:
    for line in f:
        name, expense = line.split()
        total_cost = total_cost + float(expense)
print(f'total_cost = {total_cost}')