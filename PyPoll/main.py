# import dependencies
import os
import csv

# set path for file
poll_csv = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# set starting lists and values
candidates = []
vote_percent = []
candidate_votes = []
voters = []
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

# open the csv
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip first row header
    next(csvreader, None)

    # convert the candidate column into a list
    for row in csvreader:
        voters.append(row[0])
            
        # add up votes for each candidate:
        if row[2] == "Khan":
            votes_khan += 1
        if row[2] == "Correy":
            votes_correy += 1
        if row[2] == "Li":
            votes_li += 1
        if row[2] == "O'Tooley":
            votes_otooley += 1

        # append list of candidates with unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])

# find the total number of votes (values) in the set
total_votes = len(voters)

# convert votes to percentage of total
khan_percent = round((votes_khan / total_votes)*100,3)
correy_percent = round((votes_correy / total_votes)*100,3)
li_percent = round((votes_li / total_votes)*100,3)
otooley_percent = round((votes_otooley / total_votes)*100,3)

# print election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Khan: {khan_percent}% ({votes_khan})")
print(f"Correy: {correy_percent}% ({votes_correy})")
print(f"Li: {li_percent}% ({votes_li})")
print(f"O'Tooley: {otooley_percent}% ({votes_otooley})")
print("--------------------------")
print("Winner: Khan")
print("--------------------------")

# export text file with results
# identify export path
export_path = os.path.join("Analysis", "Election_Results.txt")

# open the file in write mode
report = open(export_path, 'w')

# add text to .txt document
report.write("Election Results" + "\n")
report.write("--------------------------" + "\n")
report.write(f"Total Votes: {total_votes}" + "\n")
report.write("--------------------------" + "\n")
report.write(f"Khan: {khan_percent}% ({votes_khan})" + "\n")
report.write(f"Correy: {correy_percent}% ({votes_correy})" + "\n")
report.write(f"Li: {li_percent}% ({votes_li})" + "\n")
report.write(f"O'Tooley: {otooley_percent}% ({votes_otooley})" + "\n")
report.write("--------------------------" + "\n")
report.write("Winner: Khan" + "\n")
report.write("--------------------------")

# close file
report.close