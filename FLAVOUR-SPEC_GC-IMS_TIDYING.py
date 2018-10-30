#!/usr/bin/env python3

def _HelperFunction_csv():
    
    try:
        import glob, os, shutil

    except ModuleNotFoundError:
        return('''The modules "glob, os, & shutil" need to be installed to run this program.''')
    
    def _createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)

    _createFolder('./original_csv_files/')
    _createFolder('./TIDY_NumPy_files/')
    _createFolder('./TIDY_csv_files/')
    
    #--------------------------------------------------------
    
    TIDY_csvfiles = glob.glob('TIDY*.csv')    
    [shutil.move(j, './TIDY_csv_files/') for j in TIDY_csvfiles]

    #--------------------------------------------------------

    TIDY_NumPy_files = glob.glob('TIDY*.npy')
    [shutil.move(p, './TIDY_NumPy_files/') for p in TIDY_NumPy_files]
    
    #--------------------------------------------------------

    originalcsv = glob.glob('*.csv')
    [shutil.move(q, './original_csv_files/') for q in originalcsv]
        

def TidyFlavourSpec_GC_IMS(folder):
    '''Tidy csv files from the FlavourSpec Gas Chromatograph Ion Mobility Spectrometer (GC-IMS)'''
    
    # ------------------------------------------------------------------------------------------------
    try:
        import numpy as np, pandas as pd, glob, os
        os.chdir(folder)

    except ModuleNotFoundError:
        return('''The modules "numpy, pandas, tempfile, glob, & os" need to be installed to run this
        program.''')
    
    except NameError:
        return (''' \'folder\' is not defined. Make sure you type the full path to the folder with 
        quotes ''')
    
    csvfiles = glob.glob('*.csv')
    
    #-------------------------------------------------------------------------------------------------
    
    if csvfiles is not None:
        for x in csvfiles:
            d = pd.read_csv(x, sep=';', skiprows = 4, skipinitialspace = True , error_bad_lines=False) 
            d = np.array(d)        # convert from pandas dataframe to a numpy array
            d = d[:,2:]            # this removes columns 0 and 1
            np.save('TIDY_'+ x, d) # save the file as a numpy array ("outfile_name.npy", dataframe)
            np.savetxt('TIDY_'+ x, d, delimiter=",") # save as a csv ('"outfile_name.npy", dataframe, delimiter)

    _HelperFunction_csv()
            

