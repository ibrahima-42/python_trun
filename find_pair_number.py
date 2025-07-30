def find_pair_number(numbers):
    results = []
    for num in numbers:
        if num % 2 == 0:
           results.append(num)  
    return results

list_number =  [10, 15, 22, 33, 42, 55, 60, 20]

print(find_pair_number(list_number))
