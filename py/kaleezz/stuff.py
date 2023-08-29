import math
def myFnc(a,b,c,name):
    print(name)
    return a+b+c

print(myFnc(c=2,a=1,b=3,name='Sriram'))

#============


def Prime(n):
    for i in range (2, n//2):
        if( n% i==0):
            return True

Prime(8)