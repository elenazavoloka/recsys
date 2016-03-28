# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:20:05 2016

@author: elena
"""

def make_dict_inter(df_interactions):
    dic_inter={}
    for i in range(len(df_interactions)):
        name=df_interactions['user_id'][i]
        print name
        value=df_interactions['item_id'][i]
        print value
        if dic_inter.has_key(name):
            dic_inter[name].append(value)
        else:
            dic_inter[name]=value            
    return dic_inter