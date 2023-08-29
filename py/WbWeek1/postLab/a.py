arr = [1 ,3 ,7 ,5, 9]
for i in range(0,len(arr)):
    print(arr[i]+arr[i-1] , end = ',')
    i = i+1