'''python program to accept a sequence of comma seperated 4 digit binary
 numbers as input and print numbers that are divisible by 5 in a  comma seperated sequence '''

'''def binary_divisible_by_5(binary_sequence):
    binary_numbers = binary_sequence.split(',')
    divisible_by_5 = []

    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:
            divisible_by_5.append(binary_number)

    return ','.join(divisible_by_5)'''


def binDiv5(seq):
    numbers = seq.split(',')
   #  print(numbers)
    
    for i in numbers:
        #converts to binary 
        num = int(numbers,2)
        
        print(num)


seq = input('enter seq')
binDiv5(seq)

