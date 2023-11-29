number_of_wagons = int(input())
wagons = [0] * number_of_wagons

while True:
    command_line = input().split()

    if command_line[0] == 'End':
        print(wagons)
        break

    if command_line[0] == 'add':
        wagons[-1] += int(command_line[1])

    elif command_line[0] == 'insert':
        current_index = int(command_line[1])
        people = int(command_line[2])
        wagons[current_index] += people

    elif command_line[0] == 'leave':
        current_index = int(command_line[1])
        people = int(command_line[2])
        wagons[current_index] -= people

