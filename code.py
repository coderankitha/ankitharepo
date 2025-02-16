# Basic Python Code Example

# Define a function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming.")

# Main function
def main():
    # Get user input
    name = input("Enter your name: ")

    # Greet the user
    greet_user(name)

    # Simple arithmetic operations
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"

    # Display results
    print(f"The sum of {num1} and {num2} is: {sum}")
    print(f"The difference between {num1} and {num2} is: {difference}")
    print(f"The product of {num1} and {num2} is: {product}")
    print(f"The quotient of {num1} and {num2} is: {quotient}")

    # Use a loop to display numbers from 1 to 5
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print
        print("ankitha")