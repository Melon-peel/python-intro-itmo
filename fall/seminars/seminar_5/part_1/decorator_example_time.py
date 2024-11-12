import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@time_it
def compute():
    time.sleep(1)
    return "Done!"


@time_it
def another_task():
    time.sleep(0.5)
    return "Another task done!"

print(compute())


