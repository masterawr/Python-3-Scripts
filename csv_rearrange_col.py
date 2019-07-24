import os
import glob
import pandas as pd

os.chdir("C:\workspace")
df = pd.read_csv("combined_csv.csv")
#re-arrange columns in the order ytou want
df.reindex(columns=["Title 3", "Title 1", "Title 2"]).to_csv('outfile.csv', index=False,header=True)