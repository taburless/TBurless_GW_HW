# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    # YOUR CODE HERE
    first_row = next(reader, None)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    
   # total_months = file_to_load["Profit/Losses"].sum()
    #print(total_months)
    #total_net = file_to_load.shape[0]
    #print(total_net)
    
    for row in reader:

        # Track the total
        # YOUR CODE HERE
     
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change = month_of_change + [row[0]]
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
            # Track the net change
        # YOUR CODE HERE
        #great =  net_change_list[0]
        #least = net_change_list[0]
        
        #for r in range(len(net_change_list)):

           # if net_change_list[r] >= greatest_increase:

                #greatest_increase = net_change_list[r]

                #great_month = total_months[r]

            #elif net_change_list[r] <= greatest_decrease:

                #greatest_decrease = net_change_list[r]

               # least_month = total_months[r]

                #total_net += net_change_list[r]
        # Calculate the greatest increase
        # YOUR CODE HERE
        #maximum = net_change.max()
        #greatest_increase.append(maximum)
        # Calculate the greatest decrease
        # YOUR CODE HERE
        #minimum = net_change.min()
        #greatest_decrease.append(minimum)
# Calculate the Average Net Change
# YOUR CODE HERE
net_monthly_avg = (total_net / total_months) -1
# Generate Output Summary
output = (
    f"\nFinancial Analysis\n" +
    f"----------------------------\n" +
    f"Total Months: {total_months}\n" +
    f"Total: ${total_net}\n" +
    f"Average  Change: ${net_monthly_avg:.2f}\n" +
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n" +
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
# YOUR CODE HERE
print(output)
# Export the results to text file
# YOUR CODE HERE
#zipped_data = zip(total_months, total_net, net_monthly_avg, greatest_increase, greatest_decrease) 

with open(file_to_output, "w", newline='', encoding='utf-8') as datafile:
#    writer = csv.writer(datafile)

 #   writer.writerow(["Total Months","Total","Average Change",
 #                        "Greatest Increase in Profits","Greatest Decrease in Profits"])
        
    datafile.write(output)