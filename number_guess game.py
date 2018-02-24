import random
n=20
b=int(n*random.random())+1   #create a random number between 1 & 20
c=0
while c!=b:
    c=int(input('new number:'))
    if c>0:
        if c>b:
            print('num too large')
        elif c<b:
            print('num too less')
    else:
        print('u r given up')
        break
else:
    print('congrats u made it')

