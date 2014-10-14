x = 1
while(x < 300):
    print x
    x = x + 2
    
ABC = 0
List = [1,2,'This is the third',4,5,6,7,8,9,10]
while(ABC < len(List)):
    print List[ABC]
    ABC = ABC + 1
    
import random
rand = random.randint(0,50)
keepgoing = -1
while(keepgoing != rand):
    print 'guess a number'
    keepgoing = int(raw_input())
    if keepgoing > rand:
        print "too high guess again"
    if keepgoing < rand:
        print 'too low guess again'
    if keepgoing == rand:
        print 'cangrajumaltions you won'