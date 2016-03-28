# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:26:22 2016

@author: elena
"""

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


