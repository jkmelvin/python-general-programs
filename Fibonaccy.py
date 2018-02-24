def fib(n):
    a=0
    b=1
    print(a,'\n',b)

    for x in range(n-2):
        t=a+b
        a=b
        b=t
        print('\n',t)

    return b
num= int(input('enter the number '))
fib(num)