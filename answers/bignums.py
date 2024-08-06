
def big(numbers):
    big_numbers = []
    for num in numbers:
        if num > 10:
            big_numbers.append(num)
    return big_numbers


my_list = [5, 7, 34, 5, 3, 545]

large_numbers = big(my_list)

print(large_numbers)
