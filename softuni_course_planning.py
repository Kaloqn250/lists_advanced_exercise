lessons_schedule = input().split(', ')

command_line = input()
while command_line != 'course start':
    command_split = command_line.split(':')
    command = command_split[0]
    lesson = command_split[1]

    if command == 'Add':
        if lesson not in lessons_schedule:
            lessons_schedule.insert(len(lessons_schedule), lesson)
    if command == 'Insert':
        index = int(command_split[2])
        if lesson not in lessons_schedule:
            lessons_schedule.insert(index, lesson)
    if command == 'Remove':
        if lesson in lessons_schedule:
            lessons_schedule.remove(lesson)
    if command == 'Swap':
        first_lesson = command_split[1]
        second_lesson = command_split[2]
        if first_lesson in lessons_schedule and second_lesson in lessons_schedule:
            first_index = lessons_schedule.index(first_lesson, 0, len(lessons_schedule))
            second_index = lessons_schedule.index(second_lesson, 0, len(lessons_schedule))
            lessons_schedule[first_index], lessons_schedule[second_index] =\
                lessons_schedule[second_index], lessons_schedule[first_index]
            if (first_lesson + '-Exercise') in lessons_schedule:
                exercise = lessons_schedule.pop(first_index + 1)
                lessons_schedule.insert(second_index + 1, exercise)
            if (second_lesson + '-Exercise') in lessons_schedule:
                exercise = lessons_schedule.pop(second_index + 1)
                lessons_schedule.insert(first_index + 1, exercise)
    if command == 'Exercise':
        if lesson in lessons_schedule and (command, '-', lesson) not in lessons_schedule:
            exercise_lesson = command_split[1]
            first_index = lessons_schedule.index(exercise_lesson, 0, len(lessons_schedule))
            exercise_to_append = lesson + '-' + command
            lessons_schedule.insert(first_index + 1, exercise_to_append)
        elif lesson not in lessons_schedule and (command, '-', lesson) not in lessons_schedule:
            lessons_schedule.insert(len(lessons_schedule), lesson)
            exercise_to_append = lesson + '-' + command
            lessons_schedule.insert(len(lessons_schedule), exercise_to_append)

    command_line = input()

current_index = 1
for current_lesson in lessons_schedule:
    print(f'{current_index}.{current_lesson}')
    current_index += 1

