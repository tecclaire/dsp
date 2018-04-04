#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:34:58 2017

@author: tecclaire
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import *

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])
#1
print (np.shape(A))
print (np.shape(B))
print (np.shape(C))
print (np.shape(D))
print (np.shape(u))
print (np.shape(w))
#2
print (u+v)
print (u-v)
print (6*u)
print (np.dot(u,v))
print (np.linalg.norm(u))
#3
print (A - np.matrix.transpose(C))
print (np.matrix.transpose(C)+3*D)
print (np.dot(B,A))
print (np.dot(C,B))
print (np.linalg.matrix_power(B,4))
print (np.dot(A,np.matrix.transpose(A)))
print (np.dot(np.matrix.transpose(D),D))