# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 11:52:03 2016

@author: elena
"""

from simcalc.calc_per_type_similarity import calc_per_type_similarity
def calc_user_similarity(X,Y):
    # definr cont fields 
    cont_var=[2,7,8,9,10] # career_level experience_n_entries_class experience_years_experience experience_years_in_current edu_degree
    # define categorical fields
    cat_var=[3,4,5,6] # discipline_id industry_id country region 
    # define list fields
    list_var=[1,11] # jobroles edu_fieldofstudies
    # calculate difference between items
    
    diff=calc_per_type_similarity(X,Y,cont_var, cat_var,list_var)
    
    # add names to columns
    total_ind_list=cont_var+cat_var+list_var
    new_col_names=[ X.index[i] for i in total_ind_list ]
    diff.columns=new_col_names
    return diff