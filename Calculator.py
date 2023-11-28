def add(u, v):
    return u + v
def subtract(u, v):
    return u - v
def multiply(u, v):
    return u * v
def divide(u, v):
    return u / v
print("What's the operation you would like to perform?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    option = input("What's your choice? (1/2/3/4): ")
    if option in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Please enter 1st number: "))
            n2 = float(input("Please enter 2nd number: "))
        except ValueError:
            print("Invalid input, Please enter a number!")
            continue

        if option == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif option == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif option == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif option == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        calculation_next = input("Do you want to continue your calculation? (yes/no): ")
        if calculation_next == "no":
          break
    else:
        print("Invalid Input")