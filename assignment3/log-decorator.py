# log-decorator.py
import logging
from functools import wraps

# Setup logger (only once)
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log function name
        func_name = func.__name__

        # Log positional parameters or "none"
        pos_params = list(args) if args else "none"

        # Log keyword parameters or "none"
        kw_params = kwargs if kwargs else "none"

        # Call the actual function
        result = func(*args, **kwargs)

        # Create log message
        log_msg = (f"function: {func_name} positional parameters: {pos_params} "
                   f"keyword parameters: {kw_params} return: {result}")

        # Write to the log file
        logger.info(log_msg)

        return result
    return wrapper

# Function with no parameters
@logger_decorator
def say_hello():
    print("Hello, World!")

# Function with variable positional args
@logger_decorator
def check_all_true(*args):
    return all(args)

# Function with variable keyword args
@logger_decorator
def return_logger(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    check_all_true(True, True, False)
    return_logger(key1="value1", key2=42)
