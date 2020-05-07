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
vote_percentages = []
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

        #increment the vote ti candidate's count
        candidate_votes[candidate_name] += 1

#using the with statement with open the file as a text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nelection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    #ends print with an empty sting instead of \n new line
    print(election_results, end="")
    txt_file.write(election_results)    


    #calculate percentage of total votes per candidate
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        vote_percentages.append(f"{candidate}: {vote_percentage:.2f}") 
        candidate_results = (f"{candidate}:  {vote_percentage:.1f}%,  ({votes:,})\n")
        
        #print candidate results to the terminal, and txt file
        print(candidate_results)
        txt_file.write(candidate_results)

        #determine if canditate is the current leader
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate


    #winning printout and txt file write
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)









