#This script takes an excel file and exports all the worksheets into separate CSV files
import pandas as pd
import os

#sets the working directory
os.chdir("C:\workspace")

# If sheets are in the same file. 
xlsx = pd.ExcelFile('test.xlsx')
df1 = pd.read_excel(xlsx, 'Sheet1', index=False)
df2 = pd.read_excel(xlsx, 'Sheet2', index=False)
df3 = pd.read_excel(xlsx, 'Sheet3', index=False)

# Save the DataFrame to multiple CSV files. 
df1.to_csv('Sheet1', index=False)
df2.to_csv('Sheet2', index=False)
df3.to_csv('Sheet3', index=False)


# If sheets are in different files. 
#
#df1 = pd.read_excel('path_to_file.xls', sheet_name = "Sheet1")
#df2 = pd.read_excel('path_to_file.xls', sheet_name = "Sheet2")
#
# Use pandas.concat(), pandas.merge, or DataFrame.join() to join the DataFrames
#df = df1.join(df2)