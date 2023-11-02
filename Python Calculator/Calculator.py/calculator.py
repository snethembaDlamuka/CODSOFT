def Display_operations():
    print("Simple Calculator")
    print("Available operations: ")
    print("1. Addition (+)")
    print("2. Subtration (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")


    Number_One = float(input("Enter the first number: "))
    Number_Two = float(input("Enter the second number: "))
    The_Choice = input("Enter the operation (1/2/3/4): ")
    Calculator(Number_One, Number_Two, The_Choice)


def Calculator(Number_One,Number_Two,The_Choice):
    if The_Choice == "1":
        result = Number_One + Number_Two
        print("Result: {} + {} = {}".format(Number_One,Number_Two,result))

    elif The_Choice == "2":
        result = Number_One - Number_Two
        print("Result: {} - {} = {}".format(Number_One,Number_Two,result))

    elif The_Choice == "3":
        result = Number_One * Number_Two
        print("Result: {} * {} = {}".format(Number_One,Number_Two,result))

    elif The_Choice == "4":
        if Number_Two == 0:
            print("Error") 
        else:
            result = Number_One / Number_Two
            print("Result: {} / {} = {}".format(Number_One,Number_Two,result))

    else:
        print("Invalid operation choice.Please select 1,2,3 or 4 .")  


Display_operations()                        




