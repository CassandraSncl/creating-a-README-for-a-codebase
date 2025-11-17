def hello_world():
    print("Hello world!")

hello_world()
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def subtract(a, b):
    return a - b

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

