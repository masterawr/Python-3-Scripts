#This creates a python dictionary from a CSV file 
import csv
import os

#sets the working directory
os.chdir("C:\workspace")

#first column of the csv file contains unique keys and the second column contains values
with open('my_file.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('dictionary.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader} #mydict is the new dictionary

#print to commnad line in column format
for k, v in mydict.items():
    print (f'{k:<4} {v}')
    
#write dictionary to CSV file
w = csv.writer(open('dictionary.csv', 'w', newline= '')) #the newline= '' removes spaces
for key, val in mydict.items():
    w.writerow([key, val])
