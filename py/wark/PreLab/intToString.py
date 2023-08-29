'''a = input();
print(int(a));'''

#arr



n = int(input("size"))
arr = [n]

for i in range (0,n):
    arr.append(int(input("num")))

sum = 0

for i in range(0,n):
    sum = sum + arr[i]

aver = float(sum/3)
print('aver =',int(aver))