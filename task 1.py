def are_all_numbers_different(sequence):
    return len(sequence) == len(set(sequence))


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 3, 4]  

result1 = are_all_numbers_different(numbers1)
result2 = are_all_numbers_different(numbers2)

print (result1)
print (result2)