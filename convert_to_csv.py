# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:05:26 2021

@author: Suhas Reddy
"""


import pandas as pd
import unittest
def combine_sheets(fl,f_info,out):
    """combining all the sheets in excel.
    Arguments
    ---------
    fl : String
        contains file location where we need to access the 
        input/data files and stores output file
    f_info: Dictionary
        contains file name as keys and sheet name in list format as values. 
        example: {'file_name.xlsx':['sheet_name','sheet_name1','sheet_name2']}
    out: String
         output file name which will be stored in file_loction 
    """
    # creating Empty list to store dataframe of all sheets
    all_files=[]
    
    # accessing the keys and values from file_info to read excel file
    for i in f_info.keys():
        for j in f_info[i]:
            df=pd.read_excel(fl+i,sheet_name=j)
            all_files.append(df)
        
    # concatining all the data frames containing in all files
    final_df=pd.concat(all_files,axis=0)
    
    # converting dataframe to csv file foramt
    final_df.to_csv(fl+out,index=False)
            
        
if __name__ == '__main__':
    # define file location
    file_location = 'C:\\Users\\Suhas Reddy\\Downloads\\Data\\'
    
    # creating dictionary containing file_name as keys and required sheet names as values
    file_info1={'data.xlsx':['Detail_67_1_1','Detail_67_1_1_1','Detail_67_1_1_2','Detail_67_1_1_3','Detail_67_1_1_4','Detail_67_1_1_5','Detail_67_1_1_6']}
    file_info2={'data.xlsx':['DetailVol_67_1_1','DetailVol_67_1_1_1','DetailVol_67_1_1_2','DetailVol_67_1_1_3','DetailVol_67_1_1_4','DetailVol_67_1_1_5','DetailVol_67_1_1_6']}
    file_info3={'data.xlsx':['DetailTemp_67_1_1','DetailTemp_67_1_1_1','DetailTemp_67_1_1_2'],'data_1.xlsx':['DetailTemp_67_1_1_3','DetailTemp_67_1_1_4','DetailTemp_67_1_1_5','DetailTemp_67_1_1_6']}
    
    # output file name 
    out1='detail.csv'
    out2='detailVol.csv'
    out3='detailTemp.csv'

    # calling combine_sheets function
    combine_sheets(file_location,file_info1,out1)
    #combine_sheets(file_location,file_info2,out2)
    #combine_sheets(file_location,file_info3,out3)
    
    log_file = 'log_file.txt'
    with open(log_file,"w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)