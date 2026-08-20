def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def greet(name):
    return f"Hello, {name}! Welcome to your automated CI/CD pipeline."

if __name__ == "__main__":
    print(greet("Junaid"))
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"4 * 2 = {multiply_numbers(4, 2)}")
