def summation(*numbers):
    # result = sum(numbers)
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    average = result / (len(numbers))
    return average

def minimumNumbers(*numbers):
    min = numbers[0]
    for i in range(len(numbers)):
        if numbers[i]<min:
            min = numbers[i]
    return min

# print(summation(1,2,3,4))
# print(minimumNumbers(2,5,1,0))
n = int(input("Enter how many numbers: "))
numbers=[]

for i in range(n):
    num = int(input("Enter Numbers: "))
    numbers.append(num)
print(minimumNumbers(*numbers))