traffic_density = input("Enter traffic density (low/medium/high): ").strip().lower()
emergency_vehicle = input("Is there an emergency vehicle? (yes/no): ").strip().lower()

if traffic_density == "low":
    green_time = 20
elif traffic_density == "medium":
    green_time = 40
elif traffic_density == "high":
    green_time = 60
else:
    print("Invalid traffic density input. Please enter 'low', 'medium', or 'high'.")

if emergency_vehicle == "yes":
    print("Emergency override: route receives immediate green.")
else:
    print(f"Normal green-light time: {green_time} seconds") 