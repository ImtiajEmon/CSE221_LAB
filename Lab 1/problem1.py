#!/usr/bin/env python
# coding: utf-8

# In[2]:


odd_p = 0
even_p = 0
no_p = 0
pal = 0
no_pal = 0

def isPalindrome(word):
    global pal
    global no_pal

    if len(word) == 0:
        no_pal += 1
        return "not a palindrome"
    
    N = len(word)
    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            no_pal += 1
            return "not a palindrome"

    pal += 1
    return "a palindrome"

def parity(n):
    global no_p
    global odd_p
    global even_p

    if '.' in n:
        no_p += 1
        return "cannot have parity"

    n = int(n)
    if(n % 2 == 0):
        even_p += 1
        return "has even parity"

    odd_p += 1
    return "has odd parity"


file = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 1\\input.txt")


new_file1 = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 1\\output.txt", 'w')
new_file2 = open("F:\\Academia\\Fall 2021\\CSE221\\LAB\\Lab 1\\record.txt", 'w')


for line in file:
    temp = line.split(' ')
    new_file1.write(f"{temp[0]} {parity(temp[0])} and {temp[-1].strip()} is {isPalindrome(temp[-1].strip())}\n")


per_op = (odd_p /(odd_p + even_p + no_p)) * 100
per_ep = (even_p /(odd_p + even_p + no_p)) * 100
per_np = (no_p /(odd_p + even_p + no_p)) * 100

per_pal = (pal / (pal + no_pal)) * 100
per_nopal = (no_pal / (pal + no_pal)) * 100

new_file2.write(f"Percentage of odd parity: {per_op}%\n")
new_file2.write(f"Percentage of even parity: {per_ep}%\n")
new_file2.write(f"Percentage of no parity: {per_np}%\n")
new_file2.write(f"Percentage of palindrome: {per_pal}%\n")
new_file2.write(f"Percentage of non-palindrome: {per_nopal}%\n")


file.close()
new_file1.close()
new_file2.close()


# In[ ]:




