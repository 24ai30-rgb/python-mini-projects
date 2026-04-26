try:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))

    print("What  kind of operation do you want to perform\npress + to adfdition\npress - to subtraction\npress * to multipication\npress / to divide")

    o =input("Enter the operations")

    match o:
        case "+":
            print(f"The result is {a + b}")

        case "-":
            print(f"The result is { a - b }")

        case "*":
            print(f"The result is {a * b}")

        case "/":
            print(f"The result is ( a / b)")

        case default:
            print(f"There having a some error ")

except Exception as e:
    print("Enter the valid data of a and b")                        