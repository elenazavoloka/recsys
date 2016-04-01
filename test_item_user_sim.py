# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:06:53 2016

@author: elena
"""

#import sys
#sys.path.append('C:/Users/elena/Desktop/work/recsys challenge/recsys')
import numpy as np
import pandas as pd
from data_analysis.load_my_data import load_data
from simcalc.calc_item_user_similarity import calc_item_user_similarity
n_lines=1001
df_users=load_data('C:/Users/elena/Desktop/work/recsys challenge//data/users.csv',n_lines) # length 1 500 001
df_items=load_data('C:/Users/elena/Desktop/work/recsys challenge/data/items.csv',n_lines) #length  1 358 099   


for i in range(n_lines):
    print i
    X=df_users.iloc[i,:]
    Y=df_items.iloc[i,:]
    diff_curr=calc_item_user_similarity(X,Y)
    if i==0:
        diff=diff_curr
    else:
        diff=diff.append(diff_curr,ignore_index=True)

# add test comment to check branch