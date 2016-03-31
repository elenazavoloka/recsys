# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:13:09 2016

@author: elena
"""
import pandas as pd
import numpy as np
def calc_items_similarity(X,Y):
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