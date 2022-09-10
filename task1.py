"""
Many organizations have user ids which are constrained in some way. 
Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49). 
Your task at such an organization might be to hold a record on the billing activity for each possible user. 
Write an initialization line as a single list comprehension which creates a list of all possible user ids. 
Assume the letters are all lower case.
"""

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = []

first_10 = ['aa00', 'aa01', 'aa02', 'aa03', 'aa04', 'aa05', 'aa06', 'aa07', 'aa08', 'aa09']
last_10 =  ['zz90', 'zz91', 'zz92', 'zz93', 'zz94', 'zz95', 'zz96', 'zz97', 'zz98', 'zz99']

#List comprehension creates a list of all possible user ids
answer = [l1+l2+n1+n2 for l1 in lowercase for l2 in lowercase for n1 in digits for n2 in digits]

print(answer[0:10] == first_10)
print(answer[-10::] == last_10)
assert answer[:10] == first_10
assert answer[-10::] == last_10

