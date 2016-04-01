# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:48:16 2016

@author: elena
"""

import pandas as pd
#import numpy as np

def load_data(file_path, n_lines):
    # reads the data from the file
    # splits it by columns 
    # if column has no values, inserts nan
    file=open(file_path)
    curr_line=file.readline()
#    curr_line=file.read().splitlines()
    columns=curr_line.split("\t")
    columns[-1]=columns[-1].rstrip()
    df = pd.DataFrame(index=range(0,n_lines), columns=columns)
    for i in range(0,n_lines):
        curr_line=file.readline()
        if i==33:
            stop_here=1
#        print curr_line
        values=curr_line.split("\t")
        values[-1]=values[-1].rstrip()
        if not values[-1]:
            values[-1]=float("nan")
        if 'NULL' in values:
            for ind_null in range(len(values)):
                if values[ind_null]=='NULL':
                    values[ind_null]=float("nan")
        if '' in values:
         for ind_empt in range(len(values)):
                if values[ind_empt]=='':
                    values[ind_empt]=float("nan")            
        #    print len(values)
        df.iloc[i,:]=values
    return df    

def make_dict_inter(df_interactions):
    # creates a dictionary descrubing users and their interactions (clicks) with items 
    #  {user: item: type_of_interaction}
    dic_inter={}
    for i in range(len(df_interactions)):
        name=float(df_interactions['user_id'][i])
#        print name
        value=float(df_interactions['item_id'][i])
        inter=float(df_interactions['interaction_type'][i])
#        print value
        if dic_inter.has_key(name):
            dic_inter[name].update({value: inter})
        else:
            dic_inter[name]={value: inter}            
    return dic_inter
    

            
        

    