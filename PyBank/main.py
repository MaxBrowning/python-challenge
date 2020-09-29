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

# save everything to display analysis as output data
output_data = "Financial Analysis\n"
output_data += "------------------\n"
output_data += f"Total Months: {total_months}\n"
output_data += f"Total: ${total_profit}\n"
output_data += f"Average Change: ${avg_rev_change}\n"
output_data += f"Greatest Increase in Profits: {max_increase_date} ${max_increase}\n"
output_data += f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease}"

# print output data to terminal
print(output_data)

# export text file with results
# identify export path
export_path = os.path.join("Analysis", "Financial_Analysis.txt")

# open the file in write mode
report = open(export_path, 'w')

# add text to .txt document
report.write(output_data)

# close file
report.close