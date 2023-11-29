numbers = [int(digit) for digit in input().split(', ')]

group = 10
while numbers:
    filtered_numbers = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {filtered_numbers}")
    group += 10
    numbers = [number for number in numbers if number not in filtered_numbers]
