import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            res = func(*args, **kwargs)
            logging.info(f'Function: {func.__name__}, Arguments: {args}, {kwargs}, '
                         f'Results: {res}, lead time: {time.time() - start_time:.10f} seconds')
            return res
        except Exception as e:
            logging.error(f'error in function: {func.__name__}, '
                          f'Arguments: {args}, {kwargs}, error: {e}')
            raise
    return wrapper

@log
def factorial(n):
    if n < 0:
        return 'error'
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print('factorial', n, 'равен', factorial(n))
