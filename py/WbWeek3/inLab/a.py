def checkTri(a , b , c):
    # assuming abc forms rt tringale largest = hypth
    list = sorted([a,b,c])
    if list[0]*list[0] + list[1]*list[1] == list[2]*list[2]:
        return True
    else:
        return False
    
# defined check triangle function 

a = int(input("enter +ve side a"))
b = int(input("enter +ve side b"))
c = int(input("enter +ve side c"))

if(checkTri(a,b,c)):
    print("yes the sides can form a right trinagle")
else:
    print("not possible to make a rt tringale")
