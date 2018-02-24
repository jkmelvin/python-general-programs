import numpy as nm
import time
import sys
#import matplotlib.pyplot as plt


a = nm.array([((1,2,3),(4,5,6)),((7,8,9),(2,3,4))])
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a)
print(a.reshape(3,2,2))
print(a[0:,0:,2])

print('********************get equally spaced numnbers***************************')

b = nm.linspace (1,3,10)
print(b)

print('****************find max nim sum****************************')

print (a.max())
print(a.min())
print(a.sum())

print('***************sum of axis *****************************')

print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.sum(axis=2))

print('***************root and standard deviation *****************************')

print(nm.sqrt(a))
print(nm.std(a))

print('***************basic aruthematic ops *****************************')


a = nm.array([((1,2,3),(4,5,6)),((7,8,9),(2,3,4))])
b = nm.array([((1,2,3),(4,23,6)),((7,8,9),(2,3,4))])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)


print('***************stacking *****************************')
print(nm.vstack((a,b)))
print(nm.hstack((a,b)))
print(a.ravel())


print('***************special functions *****************************')



#x =np.arange(0,3*nm.pi,.1)
#y=nm.sin(x)
#plt.plot(x,y)
#plt.show()#


print(nm.exp(a))
print(nm.log(a))
print(nm.log10(a))