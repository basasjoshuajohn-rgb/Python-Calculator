print("Python Calculator")

while True:
    print("\nChoose an operation: +  -  *  /")
    print("Type q to quit.")

    operation = input("Operation: ")

    if operation.lower() == "q":
        print("Thank you for using the calculator!")
        break

    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Try again.")
        continue

    try:
        first_number = float(input("First number: "))
        second_number = float(input("Second number: "))

        if operation == "+":
            answer = first_number + second_number
        elif operation == "-":
            answer = first_number - second_number
        elif operation == "*":
            answer = first_number * second_number
        else:
            if second_number == 0:
                print("You cannot divide by zero.")
                continue
            answer = first_number / second_number

        print("Answer:", answer)

    except ValueError:
        print("Please enter numbers only.")