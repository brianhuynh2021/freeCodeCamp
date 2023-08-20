#From the list of numbers, move 0 to the end of the list.
a = [0, 0, 0, 74, 3, 157, 9, 2, 1, 0, 6]
#Big O n^2

temp = []
zeros = []
for i in range(len(a)):
    if a[i] != 0:
        temp.append(a[i])
    else:
        zeros.append(a[i])
print(temp+zeros)
