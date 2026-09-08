# squares of numbers from 1 through 20.
values = []
for number in range(1, 6):
    values.append(number ** 2)

values_comp = [number ** 2 for number in range(1, 6)]
print(values)
print(values_comp)


# even and odd numbers from 1 through 50
evens = [x for x in range(1, 51) if x % 2 == 0]
print(evens)
odds = [x for x in range(1, 51) if x % 2 != 0]
print(odds)