# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:06:46 2016

@author: elena
"""

def calc_item_user_similarity(user_inf, item_inf):
    from simcalc.calc_per_type_similarity import calc_per_type_similarity
    # Function compare the same coloums in items and users
    
    # define indexes to use
    # define the index of the same colomns between users and items
    user_col_index=['jobroles','career_level','discipline_id','industry_id','country','region','jobroles']
    item_col_index=['title','career_level','discipline_id','industry_id','country','region','tags']
    # define continuous fields
    cont_var=[1]
    # define categorical fields
    cat_var=[2,3,4,5,6]
    # define list fields
    list_var=[0]
    # extract fields
    X=user_inf[user_col_index]
    Y=item_inf[item_col_index]
    
    # calculate similarity
    diff=calc_per_type_similarity(X,Y,cont_var, cat_var,list_var)  
   
    # rename columns   
    total_ind_list=cont_var+cat_var+list_var
    new_col_names=[user_col_index[i] for i in total_ind_list]
    diff.columns=new_col_names
    return diff
#    
