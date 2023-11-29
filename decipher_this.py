# def decipher_word():
words = input().split()

for word in words:
    number_as_string = ''
    for char in word:
        if char.isdigit():
            number_as_string += char

    first_char = chr(int(number_as_string))

    sorted_word = [character for character in word if not character.isdigit()]
    sorted_word[0], sorted_word[-1] = sorted_word[-1], sorted_word[0]
    print(f"{first_char}{''.join(sentence for sentence in sorted_word)}", end=' ')

