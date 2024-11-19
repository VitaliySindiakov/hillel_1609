# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger("logs")


def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = None
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function: {func.__name__} returned: {result}")
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception occurred in function {func.__name__}: {e}")
        return result

    return wrapper


@log_arguments_and_result
def find_el_in_list(elements: list, index: int):
        return elements[index]


find_el_in_list(["Alex", "Den", "Ivan"], 1)
find_el_in_list(["Alex", "Den", "Ivan"], 4)
