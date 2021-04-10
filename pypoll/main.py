import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join("resources", "election_data.csv")
## The lists of columns needed
votes = []
candidates = []

# Read in the CSV file and split the data
with open(csv_path, "r") as poll_data:
    csv_reader = csv.reader(poll_data, delimiter=',')
    # Skip header row
    csv_header = next(csv_reader)

    for row in csv_reader:
        votes.append(row[0])
        candidates.append(row[2])
    
    # Counting the total amount of votes in the column 
    Total_Votes = (len(votes))

    # Counting the votes for each condidate
    Khan = int(candidates.count("Khan"))
    Correy = int(candidates.count("Correy"))
    Li = int(candidates.count("Li"))
    OTooley = int(candidates.count("O'Tooley"))

    # Calculating each candiate's percentage of the vote total and round to 2 decimal points
    Khan_percent = round((Khan/Total_Votes) * 100,2)
    Correy_percent = round((Correy/Total_Votes) * 100, 2)
    Li_percent = round((Li/Total_Votes) * 100, 2)
    OTooley_percent = round((OTooley/Total_Votes) * 100, 2)

    # Comparing candiadate's vote counts to determine the winner
    if Khan > Correy > Li > OTooley:
        Winner = "Khan"
    elif Correy > Khan > Li > OTooley:
        Winner = "Correy"
    elif Li > Khan > Correy > OTooley:
        Winner = "Li"
    elif OTooley > Khan > Correy > Li:
        Winner = "OTooley"


    print("Elections Results")
    print("--------------------------")
    print("Total Votes: " + str(Total_Votes))
    print("--------------------------")
    print("Khan: " + str(Khan_percent) + "% " + str(Khan))
    print("Correy: " + str(Correy_percent) + "% " + str(Correy))
    print("Li: " + str(Li_percent) + "% " + str(Li))
    print("O'Tooley: " + str(OTooley_percent) + "% " + str(OTooley))
    print("--------------------------")
    print("Winner: " + str(Winner))
    print("--------------------------")

# Wrinting to a new text file
save_path = 'C:\\Users\\peter\\Desktop\\python-challenge\\pypoll\\analysis'
file_name = "Election Analysis.txt"

election_file = os.path.join(save_path, file_name)
print(election_file)

election_file = open(election_file, "w")
election_file.write("Elections Results")
election_file.write("\n--------------------------")
election_file.write("\nTotal Votes: " + str(Total_Votes))
election_file.write("\n--------------------------")
election_file.write("\nKhan: " + str(Khan_percent) + "% " + str(Khan))
election_file.write("\nCorrey: " + str(Correy_percent) + "% " + str(Correy))
election_file.write("\nLi: " + str(Li_percent) + "% " + str(Li))
election_file.write("\nO'Tooley: " + str(OTooley_percent) + "% " + str(OTooley))
election_file.write("\n--------------------------")
election_file.write("\nWinner: " + str(Winner))
election_file.write("\n--------------------------")
election_file.close
