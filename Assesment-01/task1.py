def calculate_statistics(*numbers):
    n = len(numbers)
    
    #Calculate Mean
    total = 0
    for num in numbers:
        total+=num
    mean = total / n
    
    #Calculate Median
    sorted_numbers = sorted(numbers)
    if n % 2 == 1:
        median = sorted_numbers[n//2]
    else :
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    
    #Calculate Standard Deviation
    v_sum = 0
    for num in numbers:
        v_sum+=(num - mean)**2
    
    variance = v_sum / n
    standard_deviation = variance**0.5
    
    #Round them to 3 decimal place
    return{
        'mean': round(mean,3),
        'median': round(median,3),
        'std_dev': round(standard_deviation,3)
    }
    
print(calculate_statistics(1, 2, 3, 4, 5))
# Output: {'mean': 3.0, 'median': 3.0, 'std_dev': 1.414}
print(calculate_statistics(10, 15, 20, 25, 30, 35))
# Output: {'mean': 22.5, 'median': 22.5, 'std_dev': 9.354}