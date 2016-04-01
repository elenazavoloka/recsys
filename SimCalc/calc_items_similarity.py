# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:13:09 2016

@author: elena
"""
from simcalc.calc_per_type_similarity import calc_per_type_similarity
def calc_items_similarity(X,Y):
    # definr cont fields 
    cont_var=[2,7,8,11] # career_level latitude longitude created_at
    # define categorical fields
    cat_var=[3,4,5,6,9] # discipline_id industry_id country region employment
    # define list fields
    list_var=[1,10] # title tags
    # calculate difference between items
    diff=calc_per_type_similarity(X,Y,cont_var, cat_var,list_var)
    # add names to columns
    total_ind_list=cont_var+cat_var+list_var
    new_col_names=[ X.index[i] for i in total_ind_list ]
    diff.columns=new_col_names
    return diff