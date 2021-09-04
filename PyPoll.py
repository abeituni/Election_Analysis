#The data we need to retrieve
#1 The total number of votes cast
#2 A complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won
#5 The winner of the election based on popular vote
#Importing Depedencies(?)----
import csv
import os
#Command Line
#assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
import random
import numbers
#Create a filename variable to direct or inderect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: perform analysis
    print(election_data)


































#Close the file
election_data.close()