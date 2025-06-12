

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# result = num1 + num2
# print(result)

# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))
# result=num1-num2
# print(result)

# num1=float(input("enter the first number"))
# num2=float(input("enter the second number"))
# result=num1*num2
# print(result)

# num1=float(input("enter the first number"))
# num2=float(input("enter the second number"))
# result=num1/num2
# print(result)



# simple code



# print("Select Operators")
# print(
#     "1. Addition"

#     "2. Subtraction"

#     "3. Multiplication"

#     "4. Division"
# )
# # operators = float(input("Enter choice of operation 1/2/3/4: "))
# choice = input("Enter choice (1/2/3/4): ")

# num1=float(input("enter first number: "))
# num2=float(input("enter second number:"))
# if choice == "1":
#     print(add(num1, num2))
    
# elif choice == ("2"):
#     result=num1-num2
#     print("Result:", result)


# elif choice == ("3"):
#     result=num1*num2
#     print("Result:", result)


# elif choice == ("4"):
#     result=(num1/num2)
#     print("Result:", result)

# else:
#     print("invalid input")



# with function


def add (num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def devide (num1,num2):
    return num1/num2

print("Select Operators")
print(
    "1. Addition"

    "2. Subtract"

    "3. Multiply"

    "4. Devide"
)

choice = input("Enter choice (1/2/3/4): ")

num1=float(input("enter first number: "))
num2=float(input("enter second number:"))
if choice == "1":
    print(add(num1, num2))
    
elif choice == ("2"):
    print(subtract(num1,num2))
    
elif choice == ("3"):
    print(multiply(num1,num2))
    
elif choice == ("4"):
    print(devide(num1,num2))

else:
    print("invalid input")


