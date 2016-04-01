# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:33:02 2016

@author: elena
"""

###Cheatsheet
#empty data frame
diff = pd.DataFrame(np.nan, index=[0], columns=['0','1','2','3','4','5','6','7'])
# extract elements
diff.iloc[0,:]
# add new rows to data frame
diff=diff.append(diff_curr,ignore_index=True)
# Check if it is a string 
isinstance(X.iloc[list_var[k]], basestring)
# check intersection 
common_elem=set(list_X).intersection(set(list_Y))
# make nan
values[ind_null]=float("nan")

#tic tic:
import time

# clear all variables from previous session
import sys
sys.modules[__name__].__dict__.clear()