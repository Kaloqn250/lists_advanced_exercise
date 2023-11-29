happiness = [int(digit) for digit in input().split()]
happiness_multiplier = int(input())

multiplied_happiness = [number * happiness_multiplier for number in happiness]
total_happiness = 0
for current_happiness in multiplied_happiness:
    total_happiness += current_happiness

average_happiness = total_happiness / len(multiplied_happiness)

happiness_above_average = [current_hap for current_hap in multiplied_happiness if current_hap >= average_happiness]

if len(happiness_above_average) >= len(multiplied_happiness) / 2:
    print(f'Score: {len(happiness_above_average)}/{len(multiplied_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happiness_above_average)}/{len(multiplied_happiness)}. Employees are not happy!')
