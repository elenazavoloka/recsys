# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:15:34 2016

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
n_lines=30000
#df_users=load_data('../data/users.csv',n_lines) # length 1 500 001
#df_items=load_data('../data/items.csv',n_lines) #length  1 358 099
#df_impressions=load_data('../data/impressions.csv',n_lines) # 10 130 411
df_interactions=load_data('../data/interactions.csv',n_lines) # length 8 826 679
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

# calculate number of lines in the file            
#n_lines=file_len('../data/impressions.csv')
#print n_lines

# calculate similarity between users
interaction_dict=make_dict_inter(df_interactions)
all_users=interaction_dict.keys()
type_sim='cosine'
type_inter='mean0'
t = time.time()
sim=similarity_matr_subset_users(all_users, all_users,interaction_dict,type_sim,type_inter)
elapsed = time.time() - t
print elapsed
fig = plt.figure(1)
plt.hist( sum(sim>0)-1, bins=40)
plt.hist(size_user, bins=60)
plt.xlabel("N of users")
plt.ylabel("N of neighbours with non zero similarity")
print "N users with 0 neighbours with sim>0" , len(np.where(sum(sim>0)==1)[0])
# calculate the number of items clicled by a user
size_user=calc_n_items_per_user(interaction_dict)
fig = plt.figure(2)
plt.hist(size_user, bins=60)
plt.xlabel("N clicks")
plt.ylabel("N of users")

#plt.ylabel("N of neighbours with non zero similarities")
#sim=calc_similarity_dict(X, Y, type_sim, type_inter)
#print 'Similaruty= ',sim
#print sim[sim>0]
##df = pd.read_csv(file_path)
#file_item=open('items.csv')
#curr_line=file_item.readline()
#columns=curr_line.split("\t")
#print columns
#df_items=pd.DataFrame(index=range(0,n_lines), columns=columns)
