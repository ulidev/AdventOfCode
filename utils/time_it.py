import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start timer
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # End timer
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds")
        return result  # Return the original function's result
    return wrapper