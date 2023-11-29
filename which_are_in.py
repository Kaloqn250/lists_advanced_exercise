first_sequence = input().split(', ')
second_sequence = input().split(', ')

filtered_sequence = []
for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            filtered_sequence.append(first_word)
            break

print(filtered_sequence)
