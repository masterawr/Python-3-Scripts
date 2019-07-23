import os
import glob
import pandas as pd

#Change “/mydir” to your desired working directory
os.chdir("C:\workspace")

#Match the pattern (‘csv’) and save the list of file names in the ‘all_filenames’ variable
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
