#a^2 +b^2 =c^2
 from math import sqrt
n=int(input('Maximal num:'))
for a in range (1,n+1):
    for b in range (a,n):
        c_square=a**2+b**2
        c=int(sqrt(c_square))
        if ((c**2 - c_square)==0):
            print(a,b,c)