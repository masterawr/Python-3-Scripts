#Compare 2 excel files using Python and Pandas
import pandas as pd
import os

#choosing the workspace
os.chdir("C:\workspace")

df1 = pd.read_excel('excel1.xlsx') #excel doc 1
df2 = pd.read_excel('excel2.xlsx') #excel doc 2

difference = df1[df1!=df2]
print (difference)

#prints the differences in the ouptut csv file
difference.to_csv('output.csv', index=False)