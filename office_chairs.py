def free_chairs(rooms):
    total_chairs = 0
    for index_if_room in range(1, rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference < 0:
            print(f'{abs(difference)} more chairs needed in room {index_if_room}')

        total_chairs += difference
    return total_chairs


number_of_rooms = int(input())
total_free_chairs = free_chairs(number_of_rooms)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
