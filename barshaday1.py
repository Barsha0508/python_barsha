#Q.1 print helloworld

print("helloworld")

#Q.2 describe local variable and global variable code

def greet(name):
    local_var = "Hello, "  # Local variable
    print(local_var + name)

greet("John")

global_var = "Hello, "  # Global variable

def greet(name):
    print(global_var + name)

greet("meryy")
print(global_var)  # Accessible outside the function

#Q.3 Write a code that describe Indentation error
print("hello world") #indentation error

#Q.4 write a code that describe local and global variable with same name

 #Global variable
x = 10

def print_x():
    # Local variable with the same name
    x = 20
    print("Local x:", x)

print_x()
print("Global x:", x)

#Q.5 Write a code for string, int and float input.

#string input
string_input = input("enter the string:")
print("entered string:",string_input)
#int input
int_input = int(input("enter the integer:"))
print("entered int:",int_input)
#float input
float_input = input("enter the float:")
print("entered float:",float_input)






