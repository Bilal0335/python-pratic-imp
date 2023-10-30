# Python program to demonstrate
# swapping of two variables
user_input_1 = input("enter First Number: ")
user_input_2= input("enter Secon Number: ")

# Swapping of two variables
# Using third variable

temp = user_input_1
user_input_1 = user_input_2
user_input_2 = temp

print(f"you are swapping number : "+ user_input_1)
print(f"you are swapping number : "+ user_input_2)


# Or 


# Python program to demonstrate
# swapping of two variables
 
a = input("enter first number: ")
b = input("enter second number: ")

 
# Swapping of two variables
# Using third variable
a,b = b,a 
print("value of x: " + a)
print("value of y: " + b)