
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
import os, csv

#initialize variable
#csv_file = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyBank\\Resources\\budget_data.csv'
cwd = os.getcwd()
filename='Python Challenge\PyBank\Resources\\budget_data.csv'
csv_file =os.path.join(cwd,filename)

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
        
    #for each month added to total_profit calculate the change in the month
    for plm in range(len(tot_profit) - 1):
        PL_Change.append(tot_profit[ plm + 1]  - tot_profit[ plm ])

greatIncrease = max(PL_Change)    #find maximum number in the profit and lost month change
greatDecrease = min(PL_Change)    #find minimum number in the profit and lost month change

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


#output_txt = 'C:\\Users\\sonof\\UCSDProjects\\python-challenge\\Python Challenge\\PyBank\\analysis\\PyBank_Analysis_Summary.txt'
filename='Python Challenge\PyBank\\analysis\PyBank_Analysis_Summary.txt'
output_txt =os.path.join(cwd,filename)

#Print File
with open(output_txt,"w") as output:
    output.write(f'Financial Analysis \n')
    output.write(f'---------------------------------------------------\n')
    output.write(f'Total Months: {len(tot_month)} \n') 
    output.write(f'Total: ${sum(tot_profit)} \n') 
    output.write(f'Average Change: ${ round(sum(PL_Change)/len(PL_Change),2) } \n')
    output.write(f'Greatest Increase: { tot_month[ MnthGrtIncrease]}  (${ greatIncrease} ) \n') 
    output.write(f'Greatest Decrease: { tot_month[ MnthGrtDecrease]}  (${ greatDecrease }) \n') 

