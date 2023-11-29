def sorting_names():
    names = input().split(', ')
    sorted_list = sorted(names, key= lambda x: (-len(x), x))

    return sorted_list


print(sorting_names())
