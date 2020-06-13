import functools
import time

def exec_time(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("Execution time:", str(end-start) + "s")
        return result
    return decorator