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

with open(csv_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # for each row of data after the header
    for row in csvreader:
       
        tot_votes.append(row[0])
        Candidates.append(row[2])
x=0        
CanditList =[]


DistinctCandiadates = [CanditList.append(x) for x in Candidates if x not in CanditList ]

print (len(CanditList))
print (CanditList)

_dict = {'Candidate','Votes'}

_Candidates = []
_Candidates.append(_dict)
_Candidates.append('Jerry',20)

print(_Candidates)

    #for each month added to total_profit calculate the change in the month
    #for plm in range(len(tot_profit) - 1):
    #    PL_Change.append(tot_profit[ plm + 1]  - tot_profit[ plm ])


# print(f'Election Results')
# print(f'-------------------')
# print(f'Total Votes: {len(tot_votes)}') # print the total number of months




#output_txt = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyPoll\\analysis\\PyPoll_Analysis_Summary.txt'

#Print File
# with open(output_txt,"w") as output:

#     output.write(f'Election Results \n')
#     output.write(f'------------------- \n')
#     output.write(f'Total Votes: {len(tot_votes)} \n') # print the total number of months
