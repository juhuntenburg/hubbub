
# coding: utf-8

import numpy as np
from random import randint


# initializing a data structure containing the different materials to draw from

# In[22]:

bags = dict()


# In[23]:

bags['yesno'] = 7*[True] + 13*[False]


# In[45]:

bags['duration'] = [37, "as long as you can", 35, 28, 15, 31, 27, 44, 22, 2, 38, 24, 6, 3, 48, 18, 26, 46,
                    36, 14, 30, 42, 8,33, 34, 45, 16, 29, 47, 21, 50, 10, "as long as you can", 7, 32,
                    "as long as you can", 13, 23, 39, 41, 20, 25, 40, 11, 17, 1, 12, 5, 43, 19, 4, 6,
                    "as long as you can", 49]
# how to check for total length with instructions like "as long as you can"?
# where are the numbers from? how could they be generated?

# check that all durations are in there (should be 54)
print "# all durations: "+str(len(bags['duration']))

# check how many interger durations and what all integer durations add up to
int_duration = [x for x in bags['duration'] if type(x)==int]
print "# integer durations: "+str(len(int_duration))
print "total length of integer durations: "+str(sum(int_duration))

# print string durations
str_duration = [y for y in bags['duration'] if type(y)==str]
print "string durations: "+str(str_duration)


# In[ ]:

bags['hold_breath'] = ['in middle', 'after in', 'after out']
# pick duration for hold
# ,


# In[75]:

bags['fingering'] = ['trill keys 1', 'trill keys 2', '+thumb', '+thumb', '+thumb', 'trill keys 1+2',
                     1, 2, 3, 4, 5, 6, 7, 8]
# what is trill keys 1 or 2 referring to?
# len should be 14


# In[76]:

bags['fingering']


# In[66]:

covered = [{'a':[1]+7*[0], 'b':[0,1]+6*[0]},
           {'a':2*[1]+6*[0], 'b':4*[0]+2*[1]+2*[0]},
           {'a':[, 'b':}
          ]
# each list implements the 8 holes to cover, left to right

# check length of each list and if they add up to index


# In[68]:

covered[1]['b']


# IN / OUT

# piece = list (or dict)  of lenght 27
