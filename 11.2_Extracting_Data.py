#!/usr/bin/env python
# coding: utf-8

# In[5]:


#re.findall()
# If we actually want the matching string to be extracted, we use re.findall()
# [0-9]+ ; bracket zero dash nine bracket is a single digit. But then, we added a plus to it and that says one or more digits.
import re
x = "My 2 fav numbers are 23 and 29"
y = re.findall("[0-9]+", x)
print(y)
y = re.findall("[AEIOU]+", x)
print(y)


# In[10]:


# Greedy Matching : Greedy prefers the longest
import re
x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)


# In[12]:


# Non-greedy Matching: Non-greedy matching prefers the shortest
import re
x = 'From: Using the: character'
y = re.findall('^F.+?:', x)
print(y)


# In[43]:


#Fine-Tuning String Extraction_1
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 09:14:16 2008'
y = re.findall("\S+@\S+" ,x) 
# here \s is for non blank char
print(y)
# if we use '.' it will return all
y = re.findall(".+@.+" ,x) 
print(y)


# In[76]:


#Fine-Tuning String Extraction_2; this is more finely tuned.
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 09:14:16 2008'
y = re.findall("^From (\S+@\S+)" ,x) 
print(y)


# In[143]:


#re_extracting host name
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 09:14:16 2008'
y = re.findall("\@(\S+)" ,x) 
print(y)


# In[137]:


#Spam_Confidence
import re
hand = open('11.2.1_test.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)   
    if len(stuff) !=1: continue
    num = float(stuff[0])
    numlist.append(num)
    
print('Maximum:', max(numlist))


# In[154]:


#Escape Character
import re
x = 'We have just received $10.00 payment.'
y = re.findall('\$\S*', x)
print(y)


# In[ ]:





# In[ ]:




