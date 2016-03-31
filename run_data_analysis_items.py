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
from  SimCalc import calc_sim_subset, calc_similarity_dict
from SimCalc.calc_sim_subset import similarity_matr_subset_users
#from  SimCalc.calc_similarity_dict import calc_similarity_dict
from load_my_data import load_data, make_dict_inter
import matplotlib.pyplot as plt
import time
n_lines=50
#df_users=load_data('../data/users.csv',n_lines) # length 1 500 001
df_items=load_data('../data/items.csv',n_lines) #length  1 358 099
#df_impressions=load_data('../data/impressions.csv',n_lines) # 10 130 411
#df_interactions=load_data('../data/interactions.csv',n_lines) # length 8 826 679
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
def calc_n_items_per_user(inp_dict):
    n_items_user=np.zeros([len(inp_dict)])
    users=inp_dict.keys()
    for i in range(len(inp_dict)):
       n_items_user[i]=len(inp_dict[users[i]])
    return  n_items_user

def calc_items_similarity(X,Y):
    import pandas as pd
    diff = pd.DataFrame(np.nan, index=[0], columns=['title', 'career_level','discipline_id','industry_id', 'country','region','latitude','longitude','employment' ,'tags','created_at'])
    # compare cont fiends
    cont_var=['career_level','latitude','longitude','created_at']
    cat_var=['discipline_id','industry_id','country','region','employment']
    list_var=['title','tags']    
    for i in range(len(cont_var)):
         diff[[cont_var[i]]]=float(X[cont_var[i]])-float(Y[cont_var[i]])
    # compare categ fields
    for j in range(len(cat_var)):
        if X[cat_var[j]]==Y[cat_var[j]]:
            diff[[cat_var[j]]]=1
        else:
            diff[[cat_var[j]]]=0    
    # compare cont fileds         
    for k in range(len(list_var)):
        list_X=X[list_var[k]].split(',')
        list_Y=Y[list_var[k]].split(',')
        common_elem=set(list_X).intersection(set(list_Y))
        diff[list_var[k]]=len(common_elem)
    return diff
    
list_XY_title=np.empty([len(df_items), len(df_items)])
list_XY_career_level=np.empty([len(df_items), len(df_items)])
list_XY_discipline_id=np.empty([len(df_items), len(df_items)])
list_XY_industry_id=np.empty([len(df_items), len(df_items)])
list_XY_country=np.empty([len(df_items), len(df_items)])
list_XY_region=np.empty([len(df_items), len(df_items)])
list_XY_employment=np.empty([len(df_items), len(df_items)])
list_XY_tags=np.empty([len(df_items), len(df_items)])
#list_XY=[]
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
fig = plt.figure(2)
plt.hist(sum(list_XY_tags>0)-1, bins=60)
plt.xlabel("N neighbours with the same field")
plt.ylabel("N of users")