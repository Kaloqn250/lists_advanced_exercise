electrons = int(input())

electrons_list = []
for current_shel in range(1, electrons + 1):
    capacity_of_current_shel = 2 * (current_shel ** 2)
    if electrons >= capacity_of_current_shel:
        electrons_list.append(capacity_of_current_shel)
        electrons -= capacity_of_current_shel
    else:
        break

if electrons > 0:
    electrons_list.append(electrons)

print(electrons_list)
