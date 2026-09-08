marks = [78, 65, 92, 85, 48, 91]

passing_marks = [mark for mark in marks if mark >= 50]
failing_marks = [mark for mark in marks if mark < 50]

avg = sum(mark for mark in marks)/len(marks)

highest = max(marks)
lowest = min(marks)
print(f"Passing marks: {passing_marks}")
print(f"Failing marks: {failing_marks}")
print(f"Average: {avg}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}") 