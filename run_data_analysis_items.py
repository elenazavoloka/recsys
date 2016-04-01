# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:51:53 2016

@author: elena
"""

# -*- coding: utf-8 -*-

# clear all variables from previous session
#import sys
#sys.modules[__name__].__dict__.clear()
import numpy as np
import matplotlib.pyplot as plt

from data_analysis.load_my_data import load_data
from simcalc.calc_items_similarity import calc_items_similarity

n_lines=50
df_items=load_data('../data/items.csv',n_lines) #length  1 358 099

# Calculate similarity between users    
list_XY_title=np.empty([len(df_items), len(df_items)])
list_XY_career_level=np.empty([len(df_items), len(df_items)])
list_XY_discipline_id=np.empty([len(df_items), len(df_items)])
list_XY_industry_id=np.empty([len(df_items), len(df_items)])
list_XY_country=np.empty([len(df_items), len(df_items)])
list_XY_region=np.empty([len(df_items), len(df_items)])
list_XY_employment=np.empty([len(df_items), len(df_items)])
list_XY_tags=np.empty([len(df_items), len(df_items)])

for i in range(len(df_items)):
    for j in range(len(df_items)):
        X=df_items.iloc[i,:]
        Y=df_items.iloc[j,:]
        diff_XY=calc_items_similarity(X,Y)
        list_XY_title[i,j]=diff_XY['title']
        list_XY_career_level[i,j]=diff_XY['career_level']
        list_XY_discipline_id[i,j]=diff_XY['discipline_id']
        list_XY_industry_id[i,j]=diff_XY['industry_id']
        list_XY_country[i,j]=diff_XY['country']
        list_XY_region[i,j]=diff_XY['region']
        list_XY_employment[i,j]=diff_XY['employment']
        list_XY_tags[i,j]=diff_XY['tags']
        
fig = plt.figure(3)
plt.hist(sum(list_XY_title>0)-1, bins=60)
plt.xlabel("N neighbours with the same field")
plt.ylabel("N of users")