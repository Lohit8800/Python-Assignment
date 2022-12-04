#!/usr/bin/env python
# coding: utf-8
#1.What does an empty dictionary's code look like?


"""Ans: An empty dictionary is often represented by two empty curly brackets
d = {} or d = dict()"""#2.what is the value of dictionary value with key 'foo' and the value 42 ?


Ans: {'foo':42}#3.What is the most significant distinction between a dictionary and a list?


Ans: Dictionaries are represented by {} where as listed are represented by []
The Items stored in a dictionary are Unordered , while the items in a list are ordered#4.What happens if you try to access spam ['foo'] if spam is {'bar':100} ?


Ans: we will get a keyError KeyError: 'foo'#5.if a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys() ?


Ans: There is no difference . The operator checks whether a value exits as a key in the dictionary or not#6.if a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in spam.values() ?


Ans:'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.#7.what is a shortcut for the following code ?
#if 'color' not in spam: spam['color'] ='black'

"""Ans: spam.setdefault('color','black')"""
# In[1]:


#8.How do you 'pretty print' dictionary values using which modules and function ?

"""Ans: we can pretty print a dictionary using three functions

by using pprint() function of pprint module
Note: pprint() function doesnot prettify nested dictionaries
by using dumps() method of json module
by using dumps() method of yaml module"""


Cust_info = [
  {'Customer_NUM': '01', 'Cust_Name': 'Ajay', 'Cust_details': {'State':'Karnataka', 'City': 'Hassan'}},
  {'Customer_NUM': '02', 'Cust_Name': 'Balaji', 'Cust_details': {'State':'Karnataka', 'City': 'Shivamogga'}},
  {'Customer_NUM': '03', 'Cust_Name': 'Darshan', 'Cust_details': {'State':'Kerala', 'City': 'Kannur'}},
  {'Customer_NUM': '04', 'Cust_Name': 'Manoj', 'Cust_details': {'State':'Kerala', 'City': 'Kasaragouda'}}
]

print('Printing using print() function\n',Cust_info)
print('-'*70)
import pprint
print('Printing using pprint() funciton')
pprint.pprint(Cust_info)
print('-'*70)
import json
dump = json.dumps(Cust_info, indent=4)
print('Printing using dumps() method\n', dump)
print('-'*70)
import yaml
dump = yaml.dump(Cust_info)
print('Printing using dump() method\n', dump)

