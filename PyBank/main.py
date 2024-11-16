
# Modules
import os
import csv 
 
# Set path for files
file_to_load = "/Users/kflm/Desktop/Python_Challenge/PyBank/Resources/budget_data.csv"
file_to_output = "/Users/kflm/Desktop/Python_Challenge/PyBank/analysis/financial_analysis.txt"
 
# Initialize variables
total_months = 0
net_total = 0
profit_losses = []
dates = []
 
# Read the data from the CSV file
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    # Reading the header row
    csv_header = next(csvreader)
 
    # Process each row
    for row in csvreader:
        total_months += 1
        date = row[0]
        profit_loss = int(row[1])
 
        dates.append(date)
        profit_losses.append(profit_loss)
        net_total += profit_loss
 
# Calculate changes in Profit/Losses
changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]
average_change = sum(changes) / len(changes)
 
# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]
 
# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
 
# Export results to a text file
with open(file_to_output, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")