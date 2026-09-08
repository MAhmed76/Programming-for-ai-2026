rows = int(input("Enter a positive number of rows: "))

while rows <= 0:
    rows = int(input("Please enter a positive number: "))

for row in range(rows):
    for col in range(row + 1):
        print("*", end="")
    print()

print()

for row in range(rows):
    for col in range(rows - row):
        print("*", end="")
    print()    