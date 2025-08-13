# assignment2.py
import csv
import traceback
import os
from datetime import datetime
import custom_module

# Task 2: Read a CSV File
def read_employees():
    employees = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employees["fields"] = row
                else:
                    rows.append(row)
            employees["rows"] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)
    return employees

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    idx = column_index("first_name")
    return employees["rows"][row_number][idx]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[idx])
    return employees["rows"]

sorted_rows = sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    d = {}
    for key, value in zip(employees["fields"], row):
        if key != "employee_id":
            d[key] = value
    return d

# Example usage and print for Task 8:
print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result

all_employees = all_employees_dict()
print(all_employees)

# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("new secret string")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_csv_to_dict(file_path):
    data = {"fields": [], "rows": []}
    try:
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    data["rows"].append(tuple(row))
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)
    return data

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined

minutes_set = create_minutes_set()

# Task 14: Convert to datetime
def create_minutes_list():
    lst = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), lst))
    return converted

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    global minutes_list
    minutes_list.sort(key=lambda x: x[1])
    converted_back = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in converted_back:
            writer.writerow(row)
    return converted_back

write_sorted_list()
