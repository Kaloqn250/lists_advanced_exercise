def palindrome_strings():
    strings = input().split()
    palindrome_word = input()
    palindrome_list = [word for word in strings if word == word[::-1]]
    palindrome_count = 0
    for char in palindrome_list:
        if char == palindrome_word:
            palindrome_count += 1

    return palindrome_list, palindrome_count


sorted_list, count = palindrome_strings()

print(f'{sorted_list}\nFound palindrome {count} times')
