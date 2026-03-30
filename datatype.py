#data types are categories of values that we store in the memory
# 1 numeric eg inti, float, complex
# 2 string 
# 3 sequence eg list, tuple and range
# 4 mapping eg dictionary
# 5 boolean
# 6 set
#integers {int} are whole numbers from 0 to any number
my_num = 200
print(type(my_num))
#a float is any number with a decimal point eg 0.0
my_num = 200.0
print(type(my_num))
#num = 200; or var my_num = 200; if it's for c language,you would say int my_num = 200;
num1 = 2+3j
#string
# a string is a collection of characters eg our names, any value in quates is what we call a string
name = "kiconco"
my_num = "200"
#the process of creating a variable is declaring
# the process of giving a value to a variable is called initializing or assigningment
# in python we declare and initialize once or at the same time
# sequence datatype
# seq(uence are variables that can store more than one value
# a list
# a list is identified by square brackets
numbers = []
numbers2 = [5,10,15]
print(name)
print(type(numbers2))
print(numbers2)
print(numbers2[0])
print(numbers2[2])
print(numbers2[-1])
print(numbers2[1] + numbers2[-1])
my_stuff = ["ozzy",10,20,[40,60]]
print(my_stuff[3][0])
print(my_stuff[-1][-2])
animals = ["cats","dog",["fish","shark",["rat","duck",["donkey"]]]]
print(animals[2][2][0])
print(animals[-1][-1][-2])
#lists continued
my_stuff.append(1000)
print(my_stuff)
my_stuff.pop()
print(my_stuff)
#tuple is like a list takes on one or more values of any kind they are identified by () and
my_tuple = (1,2,3,4,6,8) 
print(my_tuple[4])
#mapping  is a collection of values that are identified bt their own keys or custom keys eg.
car = {"name":"Ryceroll","model":2025,"color":"gray"}
print(car.keys())
print(car.values())
#below we are updating our dictionary using a differrnt value with the same key
car["name"] = "benz"
#below im accessing all values in a dictionary
print(car.values())
print(car["model"])
# set is an unordered unique datatype
my_things = {10,20,20,10,20}
print(my_things)
my_things.add(50)
print(my_things)
my_things.discard(10)
print(my_things)
#set 0ne
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1&set2)
# union of sets
print(set1 | set2)
#difference
print(set1 - set2)
#asymetric difference
print(set1 ^ set2)
