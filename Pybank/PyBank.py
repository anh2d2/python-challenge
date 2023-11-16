# importing my dependencies
import csv
import os

# creating file paths for reading and writing
file_in = os.path.join("Pybank", "Resources", "budget_data.csv")
file_out = os.path.join("Pybank", "analysis", "budget_analysis.txt")

# tracking data
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# reading the csv
with open(file_in) as finance_data:
    reader = csv.reader(finance_data)

    # reading header
    header = next(reader)

    # ommitting headers
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # summing the total
        total_months += 1
        total_net += int(row[1])

        # logging change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        # greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# calculating avg change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# output write up
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# printing results
print(output)

# exporting as txt
with open(file_out, "w") as txt_file:
    txt_file.write(output)
