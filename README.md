# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 - The candidate results were:
   - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
   - Diana DeGette received 73.8% of the vote and 272,892 votes.
   - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
 - The winner of the election was:
   - Diana DeGette who received 73.8% of the vote and 272,892 votes.
  
  ## Challenge Overview
  The Colorado Board of Elections has also asked that you provide some additional data points. They are interested in seeing the voter turnout for each county, the percentage of votes from each county, and the county with the highest turnout. 
  
  ## Challenge Summary
  After making some addtions to the code, the election results show that:
  - The counties were:
    - Jefferson
    - Denver
    - Arapahoe
 - The county turnouts were as follows:
   - Jefferson counted for 10.5% of the votes (38,855 votes)
   - Denver counted for 82.8% of the votes (306,055 votes)
   - Arapahoe counted for 6.7% of the votes (24,801 votes)
 - The county with the highest turnout was:
   - Denver who counted for 82.8% of the votes (306,055 votes)
   
## Election Audit Summary
Should the Colorado Board of Elections (or any other board of elections, for that matter) need to use this program to complete another election audit, there shouln't be a problem using this exact code to recreate it. The code can easily applied to different datasets, assuming the datasets has the same structure as our current dataset. However, if the board wanted to view additional data points by editing this script then that could also be done as well. For example, if the Board was interested in finding the county with the lowest voter turnout every time they ran this script then the "for" loop that we used to determine the county with the highest voter turnout could be rewritten to find the county with the lowest turnout. Another data point that the Board may be interested in seeing is how each candidate fared in each separate county. 
