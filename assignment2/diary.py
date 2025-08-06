# Task 1: Diary
import traceback

try:
    with open("diary.txt", "a") as file:
        first_input = True
        while True:
            if first_input:
                line = input("What happened today? ")
                first_input = False
            else:
                line = input("What else? ")
            
            file.write(line + "\n")
            
            if line == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    if str(e):
        print(f"Exception message: {str(e)}")
    print(f"Stack trace: {stack_trace}")
