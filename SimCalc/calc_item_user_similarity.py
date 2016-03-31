# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:06:46 2016

@author: elena
"""

def calc_item_user_similarity(user_inf, item_inf):
    # compare the same coloums:
    # define the index of the same colomns between users and items
    user_col_index=['jobroles','career_level','discipline_id','industry_id','country','region','jobroles']
    item_col_index=['title','career_level','discipline_id','industry_id','country,region,tags']
    cont_var=[1]
    cat_var=[2,3,4,5,6]
    list_var=[0]
    diff=calc_per_type_similarity(user_inf[user_col_index],item_inf[item_col_index],cont_var, cat_var,list_var)
#    
import sys
sys.path.append('C:/Users/elena/Desktop/work/recsys challenge/recsys')
from data_analysis.load_my_data import load_data

n_lines=4
df_users=load_data('C:/Users/elena/Desktop/work/recsys challenge//data/users.csv',n_lines) # length 1 500 001
df_items=load_data('C:/Users/elena/Desktop/work/recsys challenge/data/items.csv',n_lines) #length  1 358 099    
#calc_item_user_similarity(df_users, df_items)
# add test comment to check branch