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
#csv_file = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyPoll\\Resources\\election_data.csv'
cwd = os.getcwd()
FileName= 'Python Challenge\PyPoll\Resources\election_data.csv'
csv_file =os.path.join(cwd, FileName)

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
       
        tot_votes.append(row[0])  #Adds voteid to tot_votes, well use this to get the total # of votes

        if row[2] in CandidatesDict.keys(): # Add Candidates to the Dictionary and count the votes
                                            # The dictionary will hold the Candidate (from column 3)
                                            # and it will hold the value ( the sum +=1 )
            CandidatesDict[row[2]] +=1
        else:
            CandidatesDict[row[2]] =1       # if its a new Candidate lets add him and start the count to 1

#Set the Output File
#output_txt = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyPoll\\analysis\\PyPoll_Analysis_Summary.txt'
FileName='Python Challenge\PyPoll\\analysis\PyPoll_Analysis_Summary.txt'
output_txt = os.path.join(cwd, FileName)

totalvotes=len(tot_votes) #Count the total num of votes

#Print 2 File & to Screen (:D )---------------------------------------------------------------------------
with open(output_txt,"w") as output:
    print(f'Election Results')
    output.write(f'Election Results \n')
    print(f'-------------------------')
    output.write(f'------------------------- \n')
    print(f'Total Votes: {len(tot_votes)}') # print the total number of votes
    output.write(f'Total Votes: {len(tot_votes)} \n') # print the total number of months
    print(f'-------------------------')
    output.write(f'------------------------- \n')

    maxVotes =0 #initialize to find out who had the most votes

    for CandidatesDict, VotesDict in CandidatesDict.items():    #going throught the dictionary and pulling the items 
                                                                #for candidate and votes
        print(f'{CandidatesDict}: {float(VotesDict/totalvotes*100):.3f}% ({VotesDict})') # Print the candidate, the % of votes, #of Votes
        output.write(f'{CandidatesDict}: {float(VotesDict/totalvotes*100):.3f}% ({VotesDict}) \n') #Print to file

        if VotesDict >= maxVotes: # check to see who has the most votes the bigger number will win
            maxVotes=VotesDict
            WinCanidate =CandidatesDict

    print(f'-------------------------')
    output.write(f'------------------------- \n')    
    print(f'Winner: {WinCanidate}')
    output.write(f'Winner: {WinCanidate}\n')
    print(f'-------------------------')
    output.write(f'------------------------- \n')

