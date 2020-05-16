import os
import glob
import pandas as pd
import csv

def csv_merge(list_of_csv_file, output_path):
    # Match the pattern (‘csv’) and save the list of file names in the ‘all_filenames’ variable
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    all_students = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    all_students.to_csv( "all_students.csv", index=False, encoding='utf-8-sig')
        
if __name__ == '__main__':
    csv_merge(['class1.csv', 'class2.csv'], 'all_students.csv')