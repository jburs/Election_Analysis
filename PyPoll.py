# The data we need to retrieve
# 1. total number of votes cast
# 2. complete list of candidates who received votes
# 3. percentage of votes each candidate won
# 4. total number of votes per candidate
# 5. winner of election based on popular vote. 

import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
#ASsign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:

    #to do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #read and print headers
    headers = next(file_reader)
    print(headers, "\n")

    #for row in file_reader:








#using the with statement with open the file as a text file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello World")








