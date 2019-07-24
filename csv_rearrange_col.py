import os
import glob
import pandas as pd
#sets the working directory
os.chdir("C:\workspace")
#reads the csv file
df = pd.read_csv("combined_csv.csv")
#re-arrange columns and outputs it in a file called outfile.csv
df.reindex(columns=["Title 3", "Title 1", "Title 2"]).to_csv('outfile.csv', index=False,header=True)
