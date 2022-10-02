"""
Jasmine Yuen & Jeffrey Zou (Temporary Ducks)
SoftDev
K06 -- py-csv
Read a list of occupations and the percentages of their occurences from a .csv file.
(Read it into a dictionary)
Then return a random occupation based on the randomness weight indicated by its percentage.
2022-09-30
time spent: 1

DISCO: Learned how to read .csv files.
QCC: NONE

PROCESS:
1. import necessary libaries (csv, random)
2. initialize the dictionary and the keys it contains (the column names of the .csv file)
3. open and read the .csv file as a .DictReader object
4. while reading it, transfer contents into the dictionary
5. make sure the percentages are converted to floats before being addeed
6. return a random occupation by using random.choice(), which employs weighted randomness
7. test to see if it is actually weighted randomness
"""

import csv
import random

# initializing dictionary + keys
jobDict = {}
jobDict["Job Class"] = []
jobDict["Percentage"] = []

# opening .csv file and reading it as a .DictReader object
# adding the job class and percentage to their appropriate slots in the dictionary
# .DictReader documentation --- https://docs.python.org/3/library/csv.html
with open('occupations.csv') as f:
    r =  csv.DictReader(f)
    for row in r:
        # making sure the total percentage is not accounted for
        if (row['Job Class']!="Total"):
            jobDict["Job Class"].append(row['Job Class'])
            # making sure the percentage is a float, not a string
            jobDict["Percentage"].append(float(row['Percentage']))

# TESTING
### print(jobDict)
### return (random.choices(jobDict["Job Class"], jobDict["Percentage"]))
### random.choices() --- https://www.w3schools.com/python/ref_random_choices.asp

# TEST CASES

### TESTING RANGE OF ERROR
ary = []
times = 1000
for num in range(times):
    ary+=(random.choices(jobDict["Job Class"], jobDict["Percentage"]))

for i in range(len(jobDict['Job Class'])):
    job = jobDict['Job Class'][i]
    apercent = jobDict['Percentage'][i]
    cpercent = (ary.count(job)/times)*100
    print(job + ": " + str(cpercent) + "%")
    print("ACTUAL: " + str(apercent) + "% " + "DIFFERENCE: " + str(apercent-cpercent) + "\n")

print(random.choices(jobDict["Job Class"], jobDict["Percentage"]))

