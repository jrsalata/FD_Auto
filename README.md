# FD_Automatic
## John Salata
### November 1st, 2025

## Summary
This was a program drafted in about 30 minutes. The goal is, given a universal relation, identify the non-trivial functional dependencies (FDs).

## How to use

### Requirements
- Python 3.12+
- Pandas library (pip install pandas)

### Needed Files
- input.csv - main csv file with all of the data
- output.csv - output csv with labels either "trivial", "accepted", or "denied"

Note that we can _never guarantee_ a functional dependency. Only deny it. Accepted is just an easy term to remember.