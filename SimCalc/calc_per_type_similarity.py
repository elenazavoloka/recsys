# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:57:54 2016

@author: elena
"""
import panda as pd
import numpy as np
def calc_per_type_similarity(X,Y,cont_var, cat_var,list_var):
  diff = pd.DataFrame(np.nan, index=[0], columns=[cont_var,cat_var,list_var])
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
    