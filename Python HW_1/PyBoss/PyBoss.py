# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

# Import required packages
import csv
import os
from datetime import datetime as dt

# Files to load and output (Remember to change these)
file_to_load = os.path.join("raw_data", "employee_data.csv")
file_to_output = os.path.join("analysis", "employee_data_reformatted_attempt2.csv")

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:

        # Grab emp_ids and store it into a list
        ids = [row[0]]
        emp_ids.append(ids)

        # Grab names, split them, and store them in a temporary variable
        #split_name = row[1].split(" ")
        name = str([row[1]])
        first, last = name.split(" ")

        # Then save first and last name in separate lists
        # YOUR CODE HERE
        emp_first_names.append(first)
        emp_last_names.append(last)
        #first = row[1].split()[1]
        #last = row[2].split()[2]
        #emp_first_names.append(first)
        #emp_last_names.append(last)
        # Grab DOB and reformat it
        # YOUR CODE HERE
        #emp_dobs = emp_dobs + [row[3]]
        #date_input = emp_dobs
        #date_object = datetime.strftime(date_input, '%b/%d/%Y') )
        dob = row[2].split("-")
        year = dob[0]
        month = dob[1]
        day = dob[2]
        reform_dob = f"{month}/{day}/{year}"
        emp_dobs.append(reform_dob)
        #dto = dt.strptime(str(dob), '%Y-%m-%d')
       # new_dob = dto.strftime('%m/%d/%Y')
       #emp_dobs.append(new_dob)
        # Then store it into a list
        # YOUR CODE HERE
        #emp_dobs.append(date_object)
        # Grab SSN and reformat it
        # YOUR CODE HERE
        split_ssn = row[3]
        
        last_four = split_ssn[7:]
        print(last_four)


        
#       split_ssn[0:3] = ("*", "*", "*")
#       split_ssn[4:6] = ("*", "*")


        #last_nums = str(ssn[7:11])
        #new_ssn = "****-**-" + last_nums
        new_ssn = "*****" + last_four
#        print(new_ssn)

        
        # Then store it into a list
        # YOUR CODE HERE
        emp_ssns.append(new_ssn)
        # Grab the states and use the dictionary to find the replacement
        # YOUR CODE HERE
        state_abbrev = us_state_abbrev[row[4]]
        #state = [row[4]]
        #for key, value in us_state_abbrev.items():
                #if ( key == state ):
                    #new_state = value
                   # found = True
        
        # Then store the abbreviation into a list
        # YOUR CODE HERE
        emp_states.append(state_abbrev)
# Zip all of the new lists together
# YOUR CODE HERE
new_zip = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)

# Write all of the election data to csv
# YOUR CODE HERE
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    # Write in zipped rows
    writer.writerows(new_zip)