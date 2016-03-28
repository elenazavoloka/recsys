# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:04:08 2016

@author: elena
"""
from scipy.stats.stats import pearsonr
from scipy.spatial.distance import cosine
import numpy as np
def calc_similarity_dict(X, Y, type_sim, type_inter):
    # Calculates similarity between two elements of a dictionary X and Y
    #  X and Y- users, X.keys- items, X[key]- rating of an item by user
    #  type_sim: type of similarity metric ( pearson or cosine)
    # type_inter: type of intersection between X and Y used to calculate similarity
    # inter: intesection between common items of X and Y is taken
    # mean0: all elements of X and Y are taken and missing values imputed with 0
    item_X=X.keys()
    item_Y=Y.keys()
    if (type_inter=='inter'):
        common_elements_XY=list(set(item_X).intersection(item_Y))
    elif (type_inter=='mean0'):
        common_elements_XY=list(set(item_X)|set(item_Y))
    ratings_X=np.zeros(len(common_elements_XY))   
    ratings_Y=np.zeros(len(common_elements_XY))   

    for i in range(len(common_elements_XY)):
#        print i
        ratings_X[i]=X.get(common_elements_XY[i],0)
        ratings_Y[i]=Y.get(common_elements_XY[i],0)    
        
    if (type_sim=='pearson'):
        # calculate the pearson correlation
        distance=pearsonr(ratings_X, ratings_Y)
    elif (type_sim=='cosine'):      
        #cosine
        distance=cosine(ratings_X, ratings_Y) 
    # to make high sim=0 and low =0 we substract 1
    distance=1-distance
    return distance
# 
#X=data[1]
#Y=data[2]
#dis=calc_similarity_dict(X, Y,  'pearson','mean0')
#print dis
