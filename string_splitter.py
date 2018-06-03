#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 12:04:30 2018

@author: kash-py
"""

#splits string by list of characters
#simple usage

#string = '1.Radioactive2.Waste3.Contaminated'
#splitters = ['1.' , '2.' , '3.'  ]
#String_Splitter(string , splitters) # input
#['', 'Radioactive', 'waste', 'bee'] # output/list of words

# =============================================================================
# 
#string = '1.Radioactive2.Waste3.Contaminated'
#splitters = ['1.' , '2.' , '3.'  ]
# 
# 
# =============================================================================


def String_Splitter(string , splitters):
    arr = [string]
    for i in splitters:
        starr = []
        for sp in arr:
            starr += sp.split(i) 
            arr = starr
    return starr



# =============================================================================
# 
#print(String_Splitter(string , splitters))
# 
# 
# 
# =============================================================================





