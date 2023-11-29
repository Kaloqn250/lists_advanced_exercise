numbers = [int(digit) for digit in input().split(', ')]

even_numbers = [even_num for even_num in numbers if even_num % 2 == 0]
odd_numbers = [odd_num for odd_num in numbers if odd_num % 2 != 0]
positive_numbers = [positive_num for positive_num in numbers if positive_num >= 0]
negative_numbers = [negative_num for negative_num in numbers if negative_num < 0]

print(f'Positive: {", ".join(str(num) for num in positive_numbers)}')
print(f'Negative: {", ".join(str(num) for num in negative_numbers)}')
print(f'Even: {", ".join(str(num) for num in even_numbers)}')
print(f'Odd: {", ".join(str(num) for num in odd_numbers)}')
