def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum/len(numbers))

average(1,2,3,7,9)

