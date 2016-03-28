# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:13:00 2016

@author: elena
"""

def similarity_matr_subset_users(users_id_1,users_id_2,interaction_dict,type_sim,type_inter):
#    import pandas as pd
    import numpy as np
    from SimCalc.calc_similarity_dict  import calc_similarity_dict
    # provides similarity martix between users
    n_users_1=len(users_id_1)
    n_users_2=len(users_id_2)
    sim=np.zeros(shape=(n_users_1,n_users_2))
    for i in range(n_users_1):
        for j in range(n_users_2):
            X=interaction_dict[users_id_1[i]]
            Y=interaction_dict[users_id_2[j]]
            sim[i,j]=calc_similarity_dict(X, Y, type_sim, type_inter)
    return sim