#!/usr/bin/env python
# coding: utf-8

# Matrix multiplication

# In[38]:


import numpy as np

def Multiply_matrix(A, B):
    n = len(A)
    C = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += int(A[i][k]) * int(B[k][j])
            matrix_C.write(str(C[i][j]) + ' ')
        matrix_C.write("\n")

                           

matrix_A = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 1\\matrix_a.txt", 'r')
matrix_B = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 1\\matrix_b.txt", 'r')
matrix_C = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 1\\matrix_c.txt", 'w')  
                           
A = []
B = []
                       
for row in matrix_A:
    temp = row.split(' ')
    A.append(temp)

for row in matrix_B:
    temp = row.split(' ')
    B.append(temp)

Multiply_matrix(A, B)
                           
matrix_A.close()
matrix_B.close()
matrix_C.close()


# In[ ]:




