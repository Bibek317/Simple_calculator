# Simple Calculator project 😁😅
import math
while True:
    print("\nHello, User welcome to my simple calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. square")
    print("6. cube")
    print("7. Sqr root")
    print("8. Power of any numbers")
    print("9.Factorial")
    print("10. Exit")

    choice = input("Enter a choice (1/2/3/4/5/6/7/8/9/10): ")

    if choice == '10':
        print("Thank you for using my calculator. \nGoodbye! see you soon 😊")
        break

    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))

        if choice == '1':
            add = num1 + num2
            print(f"The addition of {num1} or {num2} is {add}")
        elif choice == '2':
            sub = num1 - num2
            print(f"The subtraction of {num1} or {num2} is {sub}")
        elif choice == '3':
            mul = num1 * num2
            print(f"The multiplication of {num1} or {num2} is {mul}")
        elif choice == '4':
            if num2 == 0:
                print("0 is not allowed. it throws error")
            else:
                div = num1 / num2
                remainder = num1 % num2
                print(f"The division of {num1} or {num2} is {div} or remainder is {remainder}")

    # for operations that need one input
    elif choice in ['5','6','7','8','9']:
      if choice == '5':
        num1 = float(input("Enter a number: "))
        sqr = num1 ** 2
        print(f"The square of {num1} is {sqr}")

    elif choice == '6':
        num1 = float(input("Enter a number: "))
        cube = num1 ** 3
        print(f"The cube of {num1} is {cube}")

    elif choice == '7':
        num1 = float(input("Enter a number: "))
        sqrt = num1 ** 0.5
        print(f"The square root of {num1} is {sqrt}")
    elif choice == '8':
          x = float(input('Enter a number:'))
          y = float(input('Enter the power of x:'))
          power = x ** y
          print(f"The power of {x} is rasied to be {power}")
    elif choice == '9':
        num3 = float(input("Enter a number:"))
        if num3 < 0 or (num3) != num3:
          print("Factorial is only for non negative integer")
        else:
          result = math.factorial(int(num3))
          print(f"The factorial of {num3} is {result}")
   
    else:
         print("Plz select a valid operation") 