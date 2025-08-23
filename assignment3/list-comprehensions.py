# list-comprehensions.py
import csv

# Read CSV into list of lists
with open("../csv/employees.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# List comprehension for employee names (skip header)
employee_names = [row[0] + " " + row[1] for row in data[1:]]

print("All employee names:")
print(employee_names)

# List comprehension filtering names with letter 'e'
names_with_e = [name for name in employee_names if 'e' in name]

print("\nNames containing 'e':")
print(names_with_e)
