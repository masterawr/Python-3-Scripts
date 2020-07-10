d =	{"brand": "Ford", "model": "Mustang", "year": 1964} # Set the dictionary as a variable
f1 = open('en_readfile.html', 'r')                   # Opens the read file for read
f2 = open('en_writefile.html', 'w')                  # Opens the write file
for line1 in f1:                                     # Searches eachline in read file for the dictionary keys
  for key1,value1 in d.items():
    line1 = line1.replace(key1, str(value1))     # Search for the keys and replaces with values
  f2.write(line1)                                  # Writes the lines with the new values in the write file
  print (line1)                                   
f1.close()                                           #closes the read file
f2.close()                                           #closes the write file
