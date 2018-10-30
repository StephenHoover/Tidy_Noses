#!/usr/bin/env python3

##################################################################################################
#                                       ALPHA-MOS-FOX-4000                                       #                              
##################################################################################################

import shutil
import glob
import os
import re
import sys

##################################################################################################
# Points script to directory path where files are located via user input

confirmation = ''

while True:
    try:
        Path2Files = input("Please type the full path to the folder with .txt files without quotes ")
        print("You entered " + str(Path2Files))
        confirmation = input("Is this correct? y/n: ")

        if confirmation == "y" or confirmation=="Y" or confirmation=="YES" or confirmation=="yes":      
            os.chdir(Path2Files)
            break
        else:
            continue
    except:
        continue

##################################################################################################
# Create folders to store different data types

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder('./original_txt_files/')

createFolder('./tidy_txt_files/')

createFolder('./tidy_csv_files/')

##################################################################################################

print('Completed path validation')

txtfiles = glob.glob('*.txt')

for i in range(0,len(txtfiles)):
    
    with open(txtfiles[i]) as f, open('tidy_'+ (str(txtfiles[i])), 'w') as tidy:
        
        for k, line in enumerate(f):

            if line.startswith('[SENSOR NAME]'):
                sname = int(k+1)
                
            try:
                if sname == k:
                    tidy.write("Time \t" + line)
            except:
                pass
                        
            if line.startswith('[SENSOR DATA]'):
                datastart = int(k+1)

            if line.startswith('[CONTROL NAME]'):
                dataend = int(k-1)
            
            try:
                if datastart <= k <= dataend:
                    tidy.write(line)
            except:
                pass

##################################################################################################
# Convert tab delimited .txt files to comma delimited .txt files
# Convert .txt files to .csv files

tidytxt = glob.glob('tidy*.txt')

for m in range(0, len(tidytxt)):
    with open(tidytxt[m]) as TabTxt, open((str(tidytxt[m]) + '.csv'), 'w') as CommaTxt:
        for line in TabTxt:
            CommaTxt.write(line.replace('\t', ','))

csvfiles = glob.glob('*.csv')

##################################################################################################
# Copy .txt files to backup folder while preserving metadata via the "shutil.copy2" command
csvfiles = glob.glob('*.csv')

for j in range(0, len(csvfiles)):
    shutil.move(csvfiles[j], Path2Files +'/tidy_csv_files/')
    
tidytxt2 = glob.glob('tidy_*.txt')

for p in range(0, len(tidytxt2)):
    shutil.move(tidytxt2[p], Path2Files +'/tidy_txt_files/')
    
originaltxt = glob.glob('*.txt')

for q in range(0, len(originaltxt)):
    shutil.move(originaltxt[q], Path2Files +'/original_txt_files/')

