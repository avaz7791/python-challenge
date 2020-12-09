# python-challenge

## Challenge Description:
Python challenge PyBank & PyPoll. These projects take an CSV file and through an iteration it will calculate
totals, percentages and display and output and an output file.

## Information
Developer: Amir Vazquez
Date: 12/6/2020

## Contributing
Pull requests are welcome. Comments on solution are also welcomed. Always looking for different ways we could solve this problem.



## PyBank Description:
	Your task is to create a Python script that analyzes the records to calculate each of the following:
	
1)	The total number of months included in the dataset
	Approach: Count of months
2)	The net total amount of "Profit/Losses" over the entire period
	Approach: Sum of Profit/Losses
3)	Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
	Approach: Change = Month 2 - Month 1, then take average of change of months
4)	The greatest increase in profits (date and amount) over the entire period
	Approach: Maximun of (changes)
5)	The greatest decrease in losses (date and amount) over the entire period
	Approach: Minimum of (changes)
	
	As an example, your analysis should look similar to the one below:
	Financial Analysis
	----------------------------
	Total Months: 86
	Total: $38,382,578
	Average  Change: $-2,315.12
	Greatest Increase in Profits: Feb-2012 ($1,926,159)
	Greatest Decrease in Profits: Sep-2013 ($-2196167)


## Instructions PyBank
Traverse to folder PyBank and execute python file main.py
The program will open the csv file located under resources folder and process the display output.
There is no input from the user requiered

## PyPoll Description	
	In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.	
		
	You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:	
		
1)	The total number of votes cast	
	Approach: count of votes	
2)	A complete list of candidates who received votes	
	Approach: count of distinct candidates who got a vote	
3)	The percentage of votes each candidate won	
	Approach: Add candidates to a Dictionary with their value. Once we capture the value we can divide that value by the total votes submited	
4)	The total number of votes each candidate won	
	Approach: table Dictionary values for each key(Candidate)	
5)	The winner of the election based on popular vote.	
	Approach: Create an if statement comparing the Max value of votes and determine the winner	
	As an example, your analysis should look similar to the one below:	
		
		Election Results
		-------------------------
		Total Votes: 3521001
		-------------------------
		Khan: 63.000% (2218231)
		Correy: 20.000% (704200)
		Li: 14.000% (492940)
		O'Tooley: 3.000% (105630)
		-------------------------
		Winner: Khan
		-------------------------
		
In addition, your final script should both print the analysis to the terminal and export a text file with the results.	
	
##Note: Not all of the data elements from the election data file are visible in this workbook because of the limitation of excel of 1M rows	

## Instructions PyPoll
Traverse to folder PyPoll and execute python file main.py
The program will open the csv file located under resources folder and process the display output.

The program will compute all of the Candidates that are in the file. If newer candiates are added it will compute those candidates as well.
This was achieved by the use of dictionary computation.

There is no input from the user requiered other than the csv file.



# Bonus

## PyBoss
Take an employee file and parse to update the file and output a new fiel with the following:

	The Name column should be split into separate First Name and Last Name columns.
	The DOB data should be re-written into MM/DD/YYYY format.
	The SSN data should be re-written such that the first five numbers are hidden from view.
	The State data should be re-written as simple two-letter abbreviations.

## PyParagrapgh
Import a text file filled with a paragraph of your choosing.
There are 3 text files that were used for testing.

Assess the passage for each of the following:
	Approximate word count.
	Approximate sentence count.
	Approximate letter count (per word).
	Average sentence length (in words).

	