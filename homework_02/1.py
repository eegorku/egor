#!/usr/bin/env python
# coding: utf-8

# In[1]:


for m in range (1,100) :
    if m % 3 == 0 and m % 5 == 0 :
        print ('FizzBuzz')
    elif m % 3 == 0 :
        print ('Fizz')
    elif m % 5 == 0 :
        print ('Buzz')
    else :
        print (m)
        


# In[ ]:




