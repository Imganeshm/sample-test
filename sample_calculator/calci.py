# Make a program of simple calculator than can addition , subtraction , multiplication and division using a functions

def add(x,y): 
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return  x * y

def divide(x,y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter your choice (1/2/3/4):")

num_1 = int(input("Enter the first number :"))
num_2 = int(input("Enter your second number :"))

if choice == '1':
    print(num_1,"+",num_2,"=", add(num_1,num_2))

elif choice == '2':
    print(num_1,"-",num_2,"=", sub(num_1,num_2))

elif choice == '3':
    print(num_1,"*",num_2,"=", multiply(num_1,num_2))

elif choice == '4':
    print(num_1,"/",num_2,"=", divide(num_1,num_2))

else:
    print("Invalid input")