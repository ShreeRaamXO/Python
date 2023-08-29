def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n - 1)

number = int(input("enter number "))
print(f"factorial of {number} is {fact(number)}")