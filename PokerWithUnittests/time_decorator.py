import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Time Decorator - Finished {func.__name__!r} in {run_time:.4f} secs")
        return run_time
    return wrapper_timer
