#print ("hello world ")
a = 2
b = 3
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print(a // b)
print (a ** b)



a = 10
b = 2
a,b = b,a
print (f"swap a = {a},b = {b} ")

boy = input (" enter the boy name ")
girl = input ("enter the girl name ")
a = boy  +  " loves "  +  girl
print(a)

a = "vivi"
print(a.upper())

name = "chandan"
print(name[2:6])
print(name [:6])
print(name[::3])



a = "vinay is a \n goog boy"
print(a)


#operators
# assignment operator
a = 10
a = a + 20
print(a)


a = 10 
b = 20
print(a == b)
print(a>b)
print(a<b)
print(a!=b)

# logical operator  and or not 
s = "chandan"
s2 = "chandanag"
print(("c"in s)and("c"in s2))
print(("v" in s) or  ( "v" in s2))
print(not("g" in s))

 #LISTS 
num = [0,1,2,3,4,5,6]
print(num[1:4]) # 1,2,3
print(num[:4])   # 
print(num[2:])
print(num[::2]) #0 , 3,6 

# FUNTION OF LISTS ( LEN SORTED SUM )
LIST = [1,2,3,34]
print(sum(LIST) )

item = [" cat ", " dog","pigion"]
item[0]= "cat"


fruits = ("banana", "apple", "orange" , "pinapple")
print(fruits[1:3]) # apple orange 
print(fruits[-1])# pinapple
print(fruits[0]) #banana
fruits.append("ananas")
print(fruits ) 

fruits = ("mango", "orange ", "pinapple",)
print("appple" in fruits)

my_dict = {
    "vinay" : " is an overthinnker ",
    "sandeep" : "is an attitude man",
    " tharun" : " is an lover boy "
}
my_dict  ["vamshi"] = " angry man"
print(my_dict)
my_dict .pop("sandeep")
print(my_dict)

time = input (" enter the time ")
if time == 8:
    print (" its break fast time ! ")
elif time == 13 :
    print(" its lunch time ! ")
elif time == 20 :
    print(" its dinner time ")
else :
    print(" its not an meal time ")

age = int (input("enter the age "))
has_voter_id  = " true "
if age >= 18 and has_voter_id :
    print("you are eligible for voting ")
else:


# OPERATORS 
# logical operator 
num1  = int(input ("enter the first number "))
num2 = int(input("enter the secound number "))
if num1>10 and num2>10 :
    print("both  numbers are greater then 10")
else:
    print("both numbers are lesser then 10")
if num1>5 and num2>5 :
    print("at least one of the number is grater then 5")
else:
    print("no number is greater then 5")
if not(num1>num2):
    print(" first number is greater then secound ")
else:
    print("first number is not greater then secound number ")

# comparison operator 
age = int(input("enter ur age "))
if age >= 18:
    print("you are an adult")
else:
    print("your are minor ")

#membership operator 
text = input ("enter the string  : ")
if 'a' in text :
    print("letter a is present ")
else:
    print("letter a is not present ")
if 'python' not in text:
    print("the string contain python")
else:
    print("the string doesnot contain python")

#LIST
# acessing list 
items = ["brue","suger","chilli powder ", "biscut"]
print(items[-1])

# modifing list
# 1... adding ellemnt
items = ["brue","suger","chilli powder ", "biscut"]
items.append("cofee powder")
print(items )

# 2... removing elements
items = ["brue","suger","chilli powder ", "biscut"]
items.remove("biscut")
print(items )

# 3... poping the elements in list
items = ["brue","suger","chilli powder ", "biscut"]
items .pop()
print(items)

# 4... insertting element at specific index
items = ["brue","suger","chilli powder ", "biscut"]
items.insert(2,"burgger")
print(items)

# functions in list 
#1... finding the length of list 
items = ["brue","suger","chilli powder ", "biscut"]
print(len(items ))

# sorting the elements in list
items = [32,22,1,4,5]
print(sorted(items))

# finding sum of list
items = [3,4,5,6]
print(sum(items ))

# methods of list
# 1...finding index of item 
items = ["brue","suger","chilli powder ", "biscut"]
print(items.index("suger"))

# 2... count of items 
items = [1,2,3,1,3,5]
print(items.count(1))

# 3... reverse the items 
items = [1,22,33,43,53]
sorted_items = sorted(items)
rev = sorted_items.reverse()
print(sorted_items)


#example
''' add new item at the end & another at the secound position 
     remove the third item from list 
     print the list after eac operation'''
# code

items = ["brue","suger","chilli powder ", "biscut"]
items.append("chiken")
print(items)
items.insert(2,"brinjal")
print(items)
items.remove("biscut")
print(items)

#exaple 2
''' sort it in decending order
    reverse the sorted list & print it '''
# code

items = [34,45,65,3,2,4,21]
items.sort()
print(items)
items.reverse()
print(items)

# TUPLES ( WESHOULD USE ONLY CURLY BRACKETS )
# 1...  acessing items in tuple 
fruits = ["mango","bannana","piapple","sapota"]
print(fruits[1])

# tuple concatination 
tuple1 = (1,2,3)
tuple2 = (4,5,6)
combine_tuple = tuple1 + tuple2
print(combine_tuple)

# tuple repetation 
repeat_tuple = (1,3)*2
print(repeat_tuple)

# checking items in tuple
tuple = ("mango","bannana","piapple","sapota")
print("mango" in tuple)

# methods
#counting how many times each item repeated
items = (1,22,3,1,2,1,1)
print(items.count(1))

# findng index of each element
items = ("mango","bannana","piapple","sapota")
print(items.index("mango"))

# SETS
# operators union| , insertion& ,  diffrence^
s1 = { 1,2,3}
s2 = {3,5,6}
print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)

# DICTONARIES
# acesing data from dictionaries
my_dict = {
        "vinay" : " student",
        "tharun" : "worker",
        "sandeep" : "good boy"
}
print (my_dict)

my_dict = {
        "vinay" : " student",
        "tharun" : "worker",
        "sandeep" : "good boy"
}
name  = input (" enter the name : ")

if name in my_dict :
    print(my_dict[name])
else:
    print(" not found ! ")
