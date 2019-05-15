import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

#create the title for the answer print out
print ("Financial Analysis")
print ("------------------")

total_months = 0
net_total = []
monthly_change = []
net_change_list = []
max_increase = ["", 0]
max_decrease = ["", 9999999999]

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    net_total = net_total + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        net_total = net_total + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        monthly_change = monthly_change + [row[0]]

        # Calculate the greatest increase
        if net_change > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = net_change

# Calculate the Average Net Change
avg_change = sum(net_change_list) / len(net_change_list)

# Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average  Change: ${avg_change:.2f}\n"
    f"Max Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Max Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)