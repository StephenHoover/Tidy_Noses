#!/usr/bin/env python3

import numpy as np
import pandas as pd
import glob
import os
import time
import re
import sys

confirmation = ''
while (confirmation !='y') or (confirmation!='Y') or (confirmation!='YES') or (confirmation!='yes'):
    try:
        Path2Files = input("Please type the full path to the folder with .nos files without quotes")  # Python 3
        print("You entered " + str(Path2Files))
        confirmation = input("Is this correct? y/n:")

        if confirmation == "y" or confirmation=="Y" or confirmation=="YES" or confirmation=="yes":      
            os.chdir(Path2Files)
            break
        else:
            continue
    except:
        continue
        
    
os.chdir(Path2Files)
print('Completed - path vaildation')

nosfiles = glob.glob('*.nos')

[os.rename(nosfiles, nosfiles.replace('.nos', '.txt')) for nosfiles in os.listdir(Path2Files) 
    if not nosfiles.startswith('.')]
txtfiles = glob.glob('*.txt')

for i in range(0, len(txtfiles)):
    with open(txtfiles[i]) as TabTxt, open('new_'+ (str(txtfiles[i])), 'w') as CommaTxt:
        for line in TabTxt:
            CommaTxt.write(line.replace('\t', ','))
print('Completed - converting tab delimited .txt files to .csv delimited .txt files')


new = glob.glob('new_*.txt')
[os.rename(new, new.replace('.txt', '.csv')) for new in os.listdir(Path2Files) 
    if not new.startswith('.')]
csvfiles = glob.glob('*.csv')
print('Completed - converting .txt files to .csv files')

[os.rename(csvfiles, csvfiles.replace('new_', '')) for csvfiles in os.listdir(Path2Files) 
    if not csvfiles.startswith('.')]

print('Completed - removing "new_" from file names')
