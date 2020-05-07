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

#global declaration
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
counties = []
county_votes = {}
best_county_turnout = ""
best_county_count = 0
best_county_percentage = 0



#open the election results and read the file.
with open(file_to_load) as election_data:

    #to do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #read and print headers
    headers = next(file_reader)
    print(headers, "\n")

    #loop over each line in election_data
    for row in file_reader:
        total_votes += 1

        #get list of candidate names, begin tracking votes for new candiate in dictionary
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #genereate list of counties by appending counties
        county_name = row[1]
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0

        #tally the current vote by candidate name, and county
        candidate_votes[candidate_name] += 1
        county_votes[county_name] += 1

#using the with open statement, open the file as a text file to write
with open(file_to_save, "w") as txt_file:

    #Opening Statement
    election_results = (
        f"\nelection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n"
        f"\nCounty Votes:\n")

    #prints election_results to the terminal, and writes to txt file. 
    print(election_results, end="")
    txt_file.write(election_results)    


    #calculate percentage of total votes per county
    for county in county_votes:
        c_votes = county_votes[county]
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
        county_results = (f"{county}:  {c_vote_percentage:.1f}%,  ({c_votes:,})\n")

        #print county results to terminal, and txt file
        print(county_results)
        txt_file.write(county_results)

        #determine which county has the highest turnout and store the leader
        if c_votes > best_county_count:
            best_county_count = c_votes
            best_county_turnout = county

    #best county printout an txt file write
    best_county_summary = (f"\n--------------------------\n"
        f"Largest County Turnout: {best_county_turnout}\n"
        f"--------------------------\n")
    print(best_county_summary)
    txt_file.write(best_county_summary)


    #calculate percentage of total votes per candidate
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}:  {vote_percentage:.1f}%,  ({votes:,})\n")
        
        #print candidate results to the terminal, and txt file
        print(candidate_results)
        txt_file.write(candidate_results)

        #determine if canditate is the current leader
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate


    #winning candidate printout and txt file write
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
