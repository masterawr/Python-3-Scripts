import pandas as pd
import datetime
import os 
os.chdir("C:\workspace")

key_match_df = pd.read_csv('my_file.csv')

#dictionary created by function
test_dic = {"John": 12, "Jake": 45, "Sarah": 31, "Lucy": 18}

#is supposed to get the current date and time however I am using this to add a column header called "Value"
now = datetime.datetime.now()
str_date = now.strftime("Value")

#finds the keys from the dictionary and inputs the associated values in the new column titled "Value"
key_match_df[str_date] = key_match_df["Key"].map(lambda x : test_dic[x])

key_match_df.to_csv('my_file.csv', index=False)