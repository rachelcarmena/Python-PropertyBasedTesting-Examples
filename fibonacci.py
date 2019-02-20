def __fibonacci_tail(number, a, b):
    if (number == 0):
        return a
    return __fibonacci_tail(number - 1, b, a + b)

def fibonacci(number):
    return __fibonacci_tail(number, 0, 1)
