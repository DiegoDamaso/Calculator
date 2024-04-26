continue_calculating = True
while continue_calculating is True:
    valid_operator = ["+", "-", "*", "/"]
    operator = input(f"Enter the operation you want (+ - * /): ")
    while operator not in valid_operator:
        operator = input("Enter the operation you want (+ - * /): ")
    try:
        num1 = int(input("Enter the 1st number: "))
    except:
        print("Invalid input. Enter a number.")
    try:
        num2 = int(input("Enter the 2st number: "))
    except:
        print("Invalid input. Enter a number.")

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        result = num1 / num2
        print(round(result, 3))
    else:
        print("")

    continue_ = input("Continue calculating? (y/n): ")
    if continue_ == "n":
        continue_calculating = False