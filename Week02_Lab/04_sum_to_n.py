n = int(input("Enter a positive integer: "))

total = 0

for number in range(1, n + 1):
    total += number

print(f"Sum from 1 to {n} = {total}")
