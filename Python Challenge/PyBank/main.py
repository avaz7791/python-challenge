
""" 
Dev: Amir Vazquez
Date: 12/6/2020
Project: PyBank 
Description: Process csv file budget_data.csv to calculate the following:
   - Total num of months
   - net total amount of profit/ losses
   - Calculate changes in profit/Losses for the period and average of changes
   - Max Profits
   - Min profits 
"""
#add libraries
import os
import csv


#initialize variable
csv_file = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyBank\\Resources\\budget_data.csv'

tot_month = []
PL_Change = []
tot_profit = []

with open(csv_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # for each row of data after the header
    for row in csvreader:
        #tot_month += 1
        tot_month.append(row[0])
        tot_profit.append(int(row[1])) #add pl column from file to total profit variable, convert 2nd column into an integer
        
       # print(row)

    #for each month added to total_profit calculate the change in the month
    for plm in range(len(tot_profit) - 1):
        PL_Change.append(tot_profit[ plm + 1]  - tot_profit[ plm ])

greatIncrease = max(PL_Change)    
greatDecrease = min(PL_Change)    

MnthGrtIncrease = PL_Change.index(greatIncrease)+1 #add one more row to get the correct max month
MnthGrtDecrease = PL_Change.index(greatDecrease)+1 #add one more row to get the correct min month

#Print to screen

print(f'Financial Analysis')
print(f'---------------------------------------------------')
print(f'Total Months: {len(tot_month)}') # print the total number of months
print(f'Total: ${sum(tot_profit)}') # print the total profit
print(f'Average Change: ${ round(sum(PL_Change)/len(PL_Change),2) }') # print the average (total pl change / total months in pl change)

#print(f'Month of Greatest Increase: {tot_month[ MnthGrtIncrease]}') # print the greatest increase value in pl change
print(f'Greatest Increase: { tot_month[ MnthGrtIncrease]}  (${ greatIncrease} )') # print the greatest increase value in pl change
print(f'Greatest Decrease: { tot_month[ MnthGrtDecrease]}  (${ greatDecrease })') # print the greatest Decrease value in pl change

