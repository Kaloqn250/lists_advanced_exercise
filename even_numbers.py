numbers = list(map(int, input().split(', ')))

digit_or_no = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))
sorted_list = list(filter(lambda i: i != 'no', digit_or_no))

print(sorted_list)
