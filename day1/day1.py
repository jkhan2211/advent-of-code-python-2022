# GEtting the data
with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]



# print(data)

# Traverse every string in our DATA
max = 0
max_2 = 0
max_3 = 0
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max: 
        max = count
    elif count > max_2:
        max_2 = count
    elif count > max_3:
        max_3 = count


print("Answer to part 1 is: ", max)
print("Answer to part 2 is: ", max+max_2+max_3)
