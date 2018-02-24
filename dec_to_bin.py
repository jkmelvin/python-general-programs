a=int(input('Enter the number which u want to convert to binary '))
x=[]
while (a!=0):
    b=a%2
    x.append(b)
    a=a//2
x.reverse()
print(x)