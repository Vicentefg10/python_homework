# Write your code here.

#Task 1: Hello
def hello ():
    return "Hello!"

print(hello())

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

print(greet("Vicente"))

# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "int_divide":
                return a // b
            case "modulo":
                return a % b
            case "power":
                return a ** b
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
    print(calc(5, 0, "divide"))

 #Task 4: Data Type Conversion
def data_type_conversion(value, to_type):
    try:
        if to_type == "int":
            return int(value)
        elif to_type == "float":
            return float(value)
        elif to_type == "str":
            return str(value)
        else:
            return "Unsupported type"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {to_type}."
    
print(data_type_conversion("123", "int"))

#Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."
    
print(grade(85, 90, 78, 92))

#Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print(repeat("Hello", 3))

#Task 7: Student Scores, Using **kwargs
def student_scores(stat_type, **kwargs):
    try:
        if stat_type == "best":
            return max(kwargs, key=kwargs.get)
        elif stat_type == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid stat type"
    except Exception:
        return "Invalid data."
    
print(student_scores("best", Alice=85, Bob=90, Charlie=78))

#Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)

print(titleize("the quick brown fox jumps over the lazy dog"))

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("python", "pyth"))

#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[1:3] == "qu":
            result.append(word[3:] + word[:3] + "ay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)

print(pig_latin("hello world this is a test"))



