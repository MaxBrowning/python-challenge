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
vote_percents = [round(percent, 2) for percent in vote_percents]

# make list of vote totals
vote_totals = []
for value in vote_tallies.values():
    vote_totals.append(value)

# compile election results data for each candidate into a list
election_results = []
for _ in range(len(candidates)):
    election_results.append(f"{candidates[_]}: {vote_percents[_]} ({vote_totals[_]})")

# identify the winner
max_votes = max(vote_tallies.values())
winner = [k for k, v in vote_tallies.items() if v == max_votes]

# save election results as output data
output_data = "Election Results\n"
output_data += "--------------------------\n"
output_data += f"Total Votes: {total_votes}\n"
output_data += "--------------------------\n"
for elem in election_results:
    output_data += f"{elem}\n"
output_data += "--------------------------\n"
output_data += f"Winner: {winner}\n"
output_data += "--------------------------"

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