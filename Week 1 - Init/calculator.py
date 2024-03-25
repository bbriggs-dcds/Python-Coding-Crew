num1 = input("Enter your first number: ")
operator = input("Enter an operation ('+', '-', '*', or '/'): ")
num2 = input("Enter your second number: ")
match operator:
    case "+":
        print(int(num1) + int(num2))
    case "-":
        print(int(num1) - int(num2))
    case "*":
        print(int(num1) * int(num2))
    case "/":
        print(int(num1) / int(num2))
    case _:
        print("Invalid operator!")