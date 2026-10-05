def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def greet(name):
    return f"Hello, {junaid}! Welcome to your automated CI/CD pipeline."

if __name__ == "__main__":
    print(greet("Junaid"))
    print(f"5 + 9 = {add_numbers(5, 9)}")
    print(f"4 * 7 = {multiply_numbers(4, 7)}")
