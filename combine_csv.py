# Takes all csv files in a folder and appends all the data into one master csv file.
import os
import glob
import pandas as pd

#sets the working directory
os.chdir("C:\workspace")

#gathers all files with the extension csv
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the working directory
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to combined_csv.csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
