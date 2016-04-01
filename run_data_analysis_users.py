# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:26:22 2016

@author: elena
"""

# clear all variables from previous session
#import sys
#sys.modules[__name__].__dict__.clear()
import numpy as np
import matplotlib.pyplot as plt

from data_analysis.load_my_data import load_data
from simcalc.calc_user_similarity import calc_user_similarity

n_lines=500
df_users=load_data('../data/users.csv',n_lines) # length 1 500 001

# Calculate similarity between users    
list_XY_jobrole=np.empty([len(df_users), len(df_users)])
list_XY_career_level=np.empty([len(df_users), len(df_users)])
list_XY_discipline_id=np.empty([len(df_users), len(df_users)])
list_XY_industry_id=np.empty([len(df_users), len(df_users)])
list_XY_country=np.empty([len(df_users), len(df_users)])
list_XY_region=np.empty([len(df_users), len(df_users)])
list_XY_fiels_studies=np.empty([len(df_users), len(df_users)])

for i in range(len(df_users)):
    for j in range(len(df_users)):
        X=df_users.iloc[i,:]
        Y=df_users.iloc[j,:]
        diff_XY=calc_user_similarity(X,Y)
        list_XY_jobrole[i,j]=diff_XY['jobroles']
        list_XY_career_level[i,j]=diff_XY['career_level']
        list_XY_discipline_id[i,j]=diff_XY['discipline_id']
        list_XY_industry_id[i,j]=diff_XY['industry_id']
        list_XY_country[i,j]=diff_XY['country']
        list_XY_region[i,j]=diff_XY['region']
        list_XY_fiels_studies[i,j]=diff_XY['edu_fieldofstudies']
#        
fig = plt.figure(3)
plt.hist(sum(list_XY_jobrole>0)-1, bins=60)
plt.xlabel("N neighbours with the same field")
plt.ylabel("N of users")


