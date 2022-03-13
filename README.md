# Election_Analysis
## Project Overview
A Colorado Borad of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The resuts for candidates were as follow:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- The winner was Diana DeGette with 73.8% (272,892) votes.

The results for counties were as follow:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
 -The winning county was Denver with 82.8% (306,055) votes. 

## Challenge Summary
Provided files could be used for the next elections. Script should be put in the folder with two subfolders with following names "Resources" and "analysis". Then changing the csv file name (in the example code provided as "new_results.csv") in line 9  to file name with new results shoudl enable to rerun the analysis for new data.
line 9:  file_to_load = os.path.join("Resources", "new_results.csv").
The the column number in new_results.csv file has different order than original file please numbers in change lines 48 and 51.
line 48: candidate_name = row[2]
line 51: county_name = row[1]
For line 48 provide the number of column that contains candidate name and subtract one eg. if candidate name is in second column provide 1.
For line 51 provide the number of column that contains county name and subtract one eg. if county name is in first column provide 0.
