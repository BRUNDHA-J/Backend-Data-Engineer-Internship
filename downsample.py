# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:21:34 2021

@author: Suhas Reddy
"""
# importing library
import pandas as pd
import unittest
def downsample(fl,fn,spm,out):
    """Downsampling.
    Arguments
    ---------
    fl : String
        contains file location where we need to access the 
        input/data files and stores output file
    fn: Dictionary
        contains the file name as keys and column name 
        required for downsampling as values. 
        example: {'file_name.csv':'column_name'}
    spm: String
         no.of seconds for one sample
         exapmle: 10s, 15s,60s etc.
    out: String
         output file name which will be stored in file_loction 
    """
    
    # Loading csv file from file location
    df = pd.read_csv(fl+list(fn.keys())[0])
    
    # converting required column from object type to datetime for downsampling
    df[list(fn.values())[0]] = pd.to_datetime(df[list(fn.values())[0]])
    
    # downsampling the data
    df_sample = df.resample(spm, on=list(fn.values())[0]).first()
    
    # storing the output in csv file format
    df_sample.to_csv(fl+out,index = False) 
    
if __name__ == '__main__':
    
    # define file location
    file_location = 'C:\\Users\\Suhas Reddy\\Downloads\\Data\\'
    
    # creating dictionary containing file_name as keys and required column as values
    file_name = {'detail.csv':'Absolute Time'}
    file_name1 = {'detailVol.csv':'Realtime'}
    file_name2 = {'detailTemp.csv':'Realtime'}
    
    # no. of seconds per sample
    spm = '60s'
    
    # output file name 
    out1='detailDownsampled.csv'
    out2='detailVolDownsampled.csv'
    out3='detailTempDownsampled.csv'
    
    # calling downsample function
    downsample(file_location,file_name,spm,out1)
    downsample(file_location,file_name1,spm,out2)
    downsample(file_location,file_name2,spm,out3)
    
    
    log_file_1 = 'log_file_1.txt'
    with open(log_file_1,"w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
    

