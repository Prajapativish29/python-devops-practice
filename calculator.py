# project-4 calculator making

num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))
choice = input("choose options: +, -, *, / : ")

if choice == "+":
    result = num1 + num2
    print(f"your ans is:{result}")
elif choice == "-":
    result = num1 - num2
    print(f"your ans is:{result}")
elif choice == "*":
    result = num1 * num2
    print(f"your ans is:{result}")
elif choice == "/":
    result = num1 / num2
    print(f"your ans is:{result}")
else:
    print("entered wrong choice.")
