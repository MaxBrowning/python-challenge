# import dependencies
import os
import csv

# set path for file
poll_csv = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# set starting lists and values
candidates = []
voters = []
vote_tallies = {}

# open the csv
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip first row header
    next(csvreader, None)

    # convert the candidate column into a list
    for row in csvreader:
        
        # add each voter ID to a list
        voters.append(row[0])
            
        # add each new candidate to a list and set their votes to 0
        if row[2] not in vote_tallies:
            vote_tallies[row[2]] = 0
            candidates.append(row[2])

        # add votes for each candidate
        vote_tallies[row[2]] += 1

# find the total number of votes (values) in the set
total_votes = len(voters)

# make list of percents for each candidate
vote_percents = []
for value in vote_tallies.values():
    vote_percents.append(value/total_votes*100)

# make list of vote totals
vote_totals = []
for value in vote_tallies.values():
    vote_totals.append(value)

for _ in range(len(candidates)):
    print(f"{candidates[_]}: {vote_percents[_]} ({vote_totals[_]})")

# save election results as output data
output_data = "Election Results\n"
output_data += "--------------------------\n"
output_data += f"Total Votes: {total_votes}\n"
output_data += "--------------------------\n"
#output_data += f"Khan: {khan_percent}% ({votes_khan})\n"
#output_data += f"Correy: {correy_percent}% ({votes_correy})\n"
#output_data += f"Li: {li_percent}% ({votes_li})\n"
#output_data += f"O'Tooley: {otooley_percent}% ({votes_otooley})\n"
output_data += "--------------------------\n"
output_data += "Winner: Khan\n"
output_data += "--------------------------\n"

#print output data to terminal
print(f"{output_data}")

# export text file with results
# identify export path
export_path = os.path.join("Analysis", "Election_Results.txt")

# open the file in write mode
report = open(export_path, 'w')

# add text to .txt document
report.write(output_data)

# close file
report.close