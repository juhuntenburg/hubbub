
import numpy as np
from random import randint
import operator

'''
Initializing a data structure implementing the bags,
containing the different materials to draw from
-----------------------------------------------------
'''

bags = dict()

''' decision maker bag'''
bags['yesno'] = 7*[True] + 13*[False]

'''durations bag'''
bags['duration'] = [x+1 for x in range(50)]
bags['duration'] += 4*[float('inf')] # as long as you can
# how to check for total length with instructions like "as long as you can"?

'''hold breath bag'''
bags['hold_breath'] = ['middle', 'after in', 'after out']
# pick duration for hold
# symbol is ,

'''fingerings bag'''
bags['fingering'] = ['trill keys 1', 'trill keys 2', 'trill keys 1+2']
# what are the numbers referring to?
bags['fingering'] += 3*['+thumb'] #why 3*?
bags['fingering'] += [x+1 for x in range(8)]

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
# how is this generated?

# print out the patterns, check length and if they add up to index
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

'''airflow bag'''
bags['airflow'] = [0, 0.5, 1]

'''mouthpiece bag'''
bags['mouthpiece'] = [0, 0.25, 0.5, 1]

'''dynamics bag'''
bags['dynamics'] = 2*[operator.lt]
# for crescendo and diminuendo, decision in which direction comes later
#bags['dynamics'] += [(x+1)*y if x < 3 else 'm'+y
#                     for x in range(4) for y in ['f','p']]
bags['dynamics'] += range(-4,0)+range(1,5)

'''articulation bag'''
bags['articulation'] = ['.', '-', '>', '>>', 'mini tongue ram @end of breath']
# what do these mean?
# does the direction of the arrows matter?
# is the double arrow ok?


'''techniques_1 bag, text and glissandi'''
# why do specifically text and glissandi go together?
# how did you choose the consonants?
bags['techniques_1'] = ['expel air', 'frustration', 'gravel', 'sigh',
                        'text sung']
bags['techniques_1'] += ['glissandi of '+str(x) for x in
                         ['air', 'gravel', 'fingering', 'whistle']]
bags['techniques_1'] += ['text spoken mouthing vowels '
                         +str(x) for x in ['a', 'e', 'i', 'o', 'u']]
bags['techniques_1'] += ['text spoken mouthing consonants '
                         +str(x) for x in ['k', 's', 'f', 'd']]
bags['techniques_1'] += ['text spoken, Tim Winton, speaking using '
                         +str(x) for x in ['voice, ordinary']+
                         ['pitch too, of air/the breath '
                          +str(y) for y in ['low', 'medium', 'high']]]

'''techniques_2 bag, everything else'''
bags['techniques_2'] = ['whistle tone / flute whistle',
                        'gravel (only out) in voice',
                        'gravel (only out) alone',
                        'whistle tooth (only out)',
                        'beating (singing+air), .5 covered',
                        'beating (singing+air), .25 covered',
                        'whistle body (i.e. lips) (in/out)',
                        'whistle sssss',
                        'spit / saliva sound']

'''
Generating the parts of the piece
----------------------------------
'''

# function to pick from the bags
def pick(bag):
    paper = bags[bag][randint(0, len(bags[bag])-1)]
    return paper

piece = []
count = 0

# continue to produce pieces as long as the total length is less than 10 min
while count < 20: # will have to be replaced by duration time lenght, testing

    count += 1
    part = dict()
    part['count'] = count

    '''in and out'''
    if count%2==0:
        part['breath'] = 1 # in breath
    else:
        part['breath'] = 0 # out breath


    '''duration'''
    part['duration'] = pick('duration')


    '''hold breath'''
    # decide whether to pick
    if pick('yesno'):
        part['hold_breath'] = {'type':pick('hold_breath')}

        # check if hold breath fits to in/out
        if ((part['breath'] and 'out' in part['hold_breath']) \
            or (not part['breath'] and 'in' in part['hold_breath'])):
            del part['hold_breath']

        # if hold breath still exists, pick timing
        else:
            # pick a duration of hold breath
            part['hold_breath']['for'] = pick('duration')

            # if hold breath is in the middle, pick a starting point that falls
            # into total duration, check whole hold breath fits into total
            # duration, otherwise pick again
            if 'middle'in part['hold_breath']['type']:
                part['hold_breath']['at'] = pick('duration')
                while part['hold_breath']['at'] > part['duration']:
                    part['hold_breath']['at'] = pick('duration')
                while part['hold_breath']['at'] + part['hold_breath']['for'] > part['duration']+1:
                    part['hold_breath']['for'] = pick('duration')


    '''airflow'''
    # decide whether to pick, otherwise ordinary = 1
    if pick('yesno'):
        part['airflow'] = pick('airflow')
    else:
        part['airflow'] = 1


    '''mouthpiece'''
    # decide whether to pick, otherwise ordinary = .25
    if pick('yesno'):
        part['mouthpiece'] = pick('mouthpiece')
    else:
        part['mouthpiece'] = .25


    '''dynamics'''
    # pick one dynamic first
    part['dynamics'] = {'base':pick('dynamics')}

    # if first is crescendo or diminuendo, pick start and end dynamic
    if part['dynamics']['base'] == operator.lt :
        # pick start and end that are not lt
        part['dynamics']['from'] = part['dynamics']['to'] = operator.lt
        while part['dynamics']['from'] == operator.lt:
            part['dynamics']['from'] = pick('dynamics')
        while part['dynamics']['to'] == operator.lt:
            part['dynamics']['to'] = pick('dynamics')

        # decide about direction and make sure start and end make sense
        swap = randint(0,1)
        while part['dynamics']['to'] part['dynamics']['base'] part['dynamics']['from']





    print part
