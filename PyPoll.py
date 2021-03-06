#The data we need to retrieve
#1 The total number of votes cast
#2 A complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won
#5 The winner of the election based on popular vote
#Importing Depedencies(?)----
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
import random
import numbers

#Add our dependenies
import csv
import os
#assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")
#Create a filename variable to direct or inderect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0
#Candidate Options
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read and Print the header row.
    headers = next(file_reader)
    #Print each row in the CSV File
    for row in file_reader:
        #2 Add to the toal vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
with open(file_to_save, "w") as txt_file:
    print(election_results, end='')
    #Save the fianl vote count to the text file.
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping thru counts
    #1 Iterate thru cnadidate list
    for candidate_name in candidate_votes:
        #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3 Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

               #Determine winning vote count and candidate
        #1 Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2 If true then set winning_count = votes and winning_percent
            #vote_ percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3 Set the winningcandidate equal to the candidate's name
            winning_candidate = candidate_name
            #To do: print out the winning candidate, vote count & percentage in terminal
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% {votes:,}\n")
        print(candidate_results, end='')
        txt_file.write(candidate_results)
    winning_candidate_summary = (
            f"-----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------\n")
    with open(file_to_save, "w") as txt_file:
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)





































#Close the file
election_data.close()