total_pokemons = [int(digit) for digit in input().split()]

all_removed_values = 0
while total_pokemons:
    command = int(input())
    new_values = []
    increase_or_decrease = 0

    if command < 0:
        first_element = total_pokemons.pop(0)
        last_element = total_pokemons[-1]
        total_pokemons.insert(0, last_element)
        increase_or_decrease = first_element
    elif command > len(total_pokemons) - 1:
        last_element = total_pokemons.pop(-1)
        first_element = total_pokemons[0]
        total_pokemons.insert(len(total_pokemons), first_element)
        increase_or_decrease = last_element
    else:
        increase_or_decrease = total_pokemons.pop(command)

    all_removed_values += increase_or_decrease
    for number in total_pokemons:
        if number > increase_or_decrease:
            new_values.append(number - increase_or_decrease)
        else:
            new_values.append(number + increase_or_decrease)
    total_pokemons = new_values


print(all_removed_values)
