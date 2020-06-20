#This creates a python dictionary from a CSV file 
import csv
import os

#sets the working directory
os.chdir("./")

#first column of the csv file contains unique keys and the second column contains values
#opens the csv file in the working directory and opens and reads it
with open('my_csvfile.csv', mode='r') as infile:
    reader = csv.reader(infile)
    #open a new text file called outfile to store the new pyhton dictionary
    with open('dictionary.txt', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader} #mydict is the new dictionary
        print (mydict, file=outfile)

# another way to print text to a text file
#f = open("output.txt", "a")
#print("Hello stackoverflow!", file=f)
#print("I have a question.", file=f)
#f.close()

#print to commnad line in column format
#for k, v in mydict.items():
#    print (f'{k:<4} {v}')
    
#write dictionary to CSV file
#w = csv.writer(open('dictionary.csv', 'w', newline= '')) #the newline= '' removes spaces
#for key, val in mydict.items():
#    w.writerow([key, val])
