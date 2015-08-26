
import numpy as np
from random import randint

'''
Initializing a data structure implementing the bags,
containing the different materials to draw from
'''

bags = dict()

''' decision maker bag'''
bags['yesno'] = 7*[True] + 13*[False]


'''durations bag'''
bags['duration'] = [37, 35, 28, 15, 31, 27, 44, 22, 2, 38, 24, 6, 3, 48, 18, 26, 46,
                    36, 14, 30, 42, 8,33, 34, 45, 16, 29, 47, 21, 50, 10, 7, 32,
                    13, 23, 39, 41, 20, 25, 40, 11, 17, 1, 12, 5, 43, 19, 4, 6,49]
bags['duration'] += 4*['as long as you can']

# how to check for total length with instructions like "as long as you can"?
# where are the numbers from? how could they be generated?

# check that all durations are in there (should be 54)
print ""
print "durations"
print "# all durations: "+str(len(bags['duration']))

# check how many interger durations and what all integer durations add up to
int_duration = [x for x in bags['duration'] if type(x)==int]
print "# integer durations: "+str(len(int_duration))
print "total length of integer durations: "+str(sum(int_duration))

# print string durations
str_duration = [y for y in bags['duration'] if type(y)==str]
print "string durations: "+str(str_duration)


'''hold breath bag'''
bags['hold_breath'] = ['in middle', 'after in', 'after out']
# pick duration for hold
# ,


'''fingerings bag'''
bags['fingering'] = ['trill keys 1', 'trill keys 2', 'trill keys 1+2']
# what are the numbers referring to?
bags['fingering'] += 3*['+thumb'] #why 3*?
bags['fingering'] += [x+1 for x in range(8)]

print ""
print "fingering"
print bags['fingering']

# additional list to implement the actual covering patterns
# each list implements the 8 holes to cover, left to right
covered = [{'a':[1]+7*[0], 'b':[0,1]+6*[0]},
           {'a':2*[1]+6*[0], 'b':4*[0]+2*[1]+2*[0]},
           {'a':3*[1]+5*[0], 'b':2*[1]+2*[0]+1*[1]+3*[0]},
           {'a':3*[1]+1*[0]+1*[1]+3*[0], 'b':1*[1]+3*[0]+3*[1]+1*[0]},
           {'a':3*[1]+1*[0]+2*[1]+2*[0], 'b':1*[0]+2*[1]+1*[0]+3*[1]+1*[0]},
           {'a':3*[1]+1*[0]+3*[1]+1*[0], 'b':1*[0]+2*[1]+1*[0]+4*[1]},
           {'a':3*[1]+1*[0]+3*[1]+1*[0]}, # what is going on with this?
           {'a':8*[1]}
          ]

# print out the patterns and check length of each list and if they add up to index
print ""
print "covered"
choices=['a','b']
for i in range(len(covered)):
    for j in range(len(covered[i])):
        lenlist=True
        sumlist=True
        if  len(covered[i][choices[j]])!=8:
            lenlist=False
        if sum(covered[i][choices[j]])!=i+1:
            sumlist=False
        print str(i+1)+choices[j]+": "+str(covered[i][choices[j]])+" "+str(lenlist)+" "+str(sumlist)


# IN / OUT

# piece = list (or dict)  of lenght 27
