# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:57:40 2020

@author: Danie
"""

def fatorial_inter(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod

print(fatorial_inter(2))

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)

print(fatorial(2))