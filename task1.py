# Task 1: Check if a Number is Even or Odd

try:
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
