""" 
Dev: Amir Vazquez
Date: 12/6/2020
Project: PyPoll 
Description: Process csv file election_data.csv to calculate the following:
    - The total number of votes cast
    - A complete list of candidates who received votes
    - The percentage of votes each candidate won
    - The total number of votes each candidate won
    - The winner of the election based on popular vote.
"""

#add libraries
import os, csv

#initialize variable
csv_file = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyPoll\\Resources\\election_data.csv'

tot_votes = []
Candidates = []
CandidatesDict = dict() #create dictionary to hold canidate name and store value

#CandidatesDict ={'Candidate':"Votes"} #add a Header to the dictionary
with open(csv_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # for each row of data after the header
    for row in csvreader:
       
        tot_votes.append(row[0])

        if row[2] in CandidatesDict.keys():
            CandidatesDict[row[2]] +=1
        else:
            CandidatesDict[row[2]] =1


totalvotes=len(tot_votes)

print(f'Election Results')
print(f'-------------------')
print(f'Total Votes: {len(tot_votes)}') # print the total number of votes
print(f'-------------------')

maxVotes =0 #initialize to find out who had the most votes
for CandidatesDict, VotesDict in CandidatesDict.items():    #going throught the dictionary and pulling the items for candidate and votes
    print(f'{CandidatesDict}: {float(VotesDict/totalvotes*100):.3f}% ({VotesDict})')

    if VotesDict >= maxVotes: # check to see who has the most votes the bigger number will win
        maxVotes=VotesDict
        WinCanidate =CandidatesDict
print(f'-------------------')
print(f'Winner: {WinCanidate}')
print(f'-------------------')

output_txt = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyPoll\\analysis\\PyPoll_Analysis_Summary.txt'

#Print File
# with open(output_txt,"w") as output:

#     output.write(f'Election Results \n')
#     output.write(f'------------------- \n')
#     output.write(f'Total Votes: {len(tot_votes)} \n') # print the total number of months
