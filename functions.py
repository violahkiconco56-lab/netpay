# a function is a named, block of code that performs a specific task.
def add():
    num1, num2 = 20, 10
    print(num1 + num2)
#  A function would be ignored untill called upon
add()
# this prints even numbers
def even():
    for number in range(10):
        if number % 2 == 0:
            print(number)
even()            
# this prints odd numbers
def odd():
    for number in range(10):
        if number % 2 != 0:
            print(number)
odd()  
# functions are self contained, meaning any variable within the function can't be accessible outside that function. e.g
num3 = 10
def my_stuff():
    num1, num2 = 30, 50
    print(num1 + num2 + num3)
my_stuff()
# print(num1)
# otherwise the variables in a function are private or local to only the funcion
def my_input():
    name = input("Please enter your name here")
    print(name)
my_input()
