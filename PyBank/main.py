# import dependencies
import os
import csv

# set path for file
bank_csv = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# make empty lists
date = []
profit_losses = []
revenue_change = []

# open the csv
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip first row header
    next(csvreader, None)

    # convert the columns into lists
    for row in csvreader:
        profit_losses.append(row[1])
        date.append(row[0])

# convert list of strings to list of integers for profit_losses
profit_losses = list(map(int, profit_losses))

# find the total number of months (values) in the set
total_months = len(profit_losses)

# find the net total amount of profits
total_profit = sum(profit_losses)

# create new list for revenue changes
for i in range(1,len(profit_losses)):
    revenue_change.append(profit_losses[i] - profit_losses[i-1])

# find average revenue change
tot_rev_change = sum(revenue_change)
num_rev_change = len(revenue_change)
avg_rev_change = round((tot_rev_change / num_rev_change),2)

# identify max increase and decrease in profits
max_increase = max(revenue_change)
max_decrease = min(revenue_change)

# identify months with max increase and decrease in profits
max_increase_date = date[revenue_change.index(max(revenue_change))]
max_decrease_date = date[revenue_change.index(min(revenue_change))]

# print everything to display analysis
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(avg_rev_change))
print("Greatest Increase in Profits: " + str(max_increase_date) + " $" + str(max_increase))
print("Greatest Decrease in Profits: " + str(max_decrease_date) + " $" + str(max_decrease))

# export text file with results
# identify export path
export_path = os.path.join("Analysis", "Financial_Analysis.txt")

# open the file in write mode
report = open(export_path, 'w')

# add text to .txt document
report.write("Financial Analysis" + "\n")
report.write("------------------" + "\n")
report.write("Total Months: " + str(total_months) + "\n")
report.write("Total: $" + str(total_profit) + "\n")
report.write("Average Change: $" + str(avg_rev_change) + "\n")
report.write("Greatest Increase in Profits: " + str(max_increase_date) + " $" + str(max_increase) + "\n")
report.write("Greatest Decrease in Profits: " + str(max_decrease_date) + " $" + str(max_decrease))

# close file
report.close