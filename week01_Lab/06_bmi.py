weight = float(input("Enter weight in KG: "))
height = float(input("Enter height in meters: "))
BMI = weight / height**2

print(round(BMI, 2))
# print(f"{BMI:.2f}")