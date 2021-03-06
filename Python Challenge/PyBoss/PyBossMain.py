""" 
Dev: Amir Vazquez
Date: 12/7/2020
Project: PyBoss
Description: Process csv file employee_data.csv to process the folowing
    - The Name column should be split into separate First Name and Last Name columns.
    - The DOB data should be re-written into MM/DD/YYYY format.
    - The SSN data should be re-written such that the first five numbers are hidden from view.
    - The State data should be re-written as simple two-letter abbreviations.
"""

#add libraries
import os, csv

#initialize variable
cwd = os.getcwd()
filename='Python Challenge\PyBoss\Resources\\employee_data.csv'
csv_file =os.path.join(cwd,filename)

# Emp ID,Name,DOB,SSN,State
# Initialize variables arrays/lists
EmpID = []
Employee_FName=[]
Employee_LName=[]
DOB=[]
SSN = []
State=[]
# EmployeeList = dict() not needed

#us_statee_abbrev dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


with open(csv_file, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        EmpID.append(row[0].split(" ")[0])                  #
        Employee_FName.append(row[1].split(" ")[0])
        Employee_LName.append(row[1].split(" ")[1])
        DOB.append(row[2].split("-")[1] + "/" + row[2].split("-")[2] + "/" + row[2].split("-")[0])
        
        State.append(us_state_abbrev[row[4]])
        #SSN.append(row[3].split("-")[0] +"-"+ row[3].split("-")[1] + "-"+ row[3].split("-")[2] )
        SSN.append("***-**"+ row[3].split("-")[2] )


Obs = zip(EmpID, Employee_FName, Employee_LName, SSN, State)  # Add variables and zip into Obs 
Observation = set(Obs)              # convert Obs into a set


#Set new file to output
filename='Python Challenge\PyBoss\employee_data_Upd.csv'
output_csv =os.path.join(cwd,filename)

#Print File
with open(output_csv,"w" , newline='', encoding='utf-8') as output:    
    csvfile = csv.writer(output, delimiter = ",")   #Set the delimiter to comma
    csvfile.writerows(Observation)                  #Use the Set Observation and write to file






