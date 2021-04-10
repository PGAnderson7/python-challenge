import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join("resources", "budget_data.csv")
## Varibles and the lists of columns
month_profit_loss = []
date = []
total_amount = 0
total_change = 0
month_start = 0
month_count = 0

# Read in the CSV file and split the data
with open(csv_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    # Skip header row
    csv_header = next(csv_reader)
    #Loop
    for row in csv_reader:
        # Month counter
        month_count = month_count + 1
        # Tracking of date/month
        date.append(row[0])
        # List of profit/losses and running total
        total_amount = total_amount + int(row[1])
        # Average change in profit/losses each month
        month_end = int(row[1])
        if month_start == 0:
            monthly_change = 0
        else:
            monthly_change = month_end - month_start
        # Store monthly profit chnge in list
        month_profit_loss.append(monthly_change)
        # Total change in profit/losses
        total_change = total_change + monthly_change
        # Reset month start for next loop
        month_start = month_end
        # Determining greatest increase and decrease from month proft/loss list
        greatest_increase = max(month_profit_loss)
        greatest_decrease = min(month_profit_loss)
        # Getting the date for greatest increase and decrease for printing
        gi_month = date[month_profit_loss.index(greatest_increase)]
        gd_month = date[month_profit_loss.index(greatest_decrease)]
# Finding the average profit/loss change and using round to only have 2 deciamals
average_change = float(round(total_change/(month_count - 1), 2))
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(gi_month) + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(gd_month) + " $" + str(greatest_decrease))

# Wrinting to a new text file
save_path = 'C:\\Users\\peter\\Desktop\\python-challenge\\pybank\\analysis'
file_name = "FinancialAnalysis.txt"

financial_analysis_file = os.path.join(save_path, file_name)
print(financial_analysis_file)

financial_analysis_file = open(financial_analysis_file, "w")
financial_analysis_file.write("Financial Analysis")
financial_analysis_file.write("\n-----------------------------")
financial_analysis_file.write("\nTotal Months: " + str(month_count))
financial_analysis_file.write("\nTotal: $" + str(total_amount))
financial_analysis_file.write("\nAverage Change: $" + str(average_change))
financial_analysis_file.write("\nGreatest Increase in Profits: " + str(gi_month) + " $" + str(greatest_increase))
financial_analysis_file.write("\nGreatest Decrease in Profits: " + str(gd_month) + " $" + str(greatest_decrease))
financial_analysis_file.close
