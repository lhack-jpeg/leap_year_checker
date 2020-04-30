# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:18:41 2020
Next 5 leap years
@author: luke-
"""
year = int(input('Enter a year:'))
if year%4 == 0:
  print ([(year+4), (year+8), (year+12), (year+16)])
else:
  if year%4 !=0:
   print([(year+(4-year%4)), (year+(4-year%4)+4), (year+(4-year%4)+8), (year+(4-year%4)+12), (year+(4-year%4)+16)])