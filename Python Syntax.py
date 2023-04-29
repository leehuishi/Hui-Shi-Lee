#****************************************************************
#****************************************************************
# Notes
#****************************************************************
#****************************************************************
#INDENTATION MATTERS

#Multiline Comments
"""
This is a comment
written in
more than just one line
"""
#-------------------------------------
#Single and Double Quotes is the same
#Variable names are case-sensitive.

#-------------------------------------
#can change type by re-declaring variable
#print type
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(type(x))

#-------------------------------------
x = 1    # int
y = 2.8  # float

#convert from int to float:
a = float(x) #it will return 1.0 type will change to float

#convert from float to int:
b = int(y) #it will return 2 it auto round down, type will change to int

#convert from float to str:
c = str(y) #it will return 2 it auto round down, type will change to int

#-------------------------------------
#Multiline Strings (three single or double quotes)
a = """Lorem ipsum dolor sit amet,
ut labore et dolore magna aliqua."""
print(a)

#-------------------------------------
#Strings are array
a = "Hello, World!"
print(a[1]) #e start from 0

#****************************************************************
#****************************************************************
# Echo variable/var_dump variable to check
#****************************************************************
#****************************************************************
print("Hello world") # to view result 

#-------------------------------------
#more for combine string printing
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #Python is awesome

#-------------------------------------
#more for calculation
x = 5
y = 10
print(x + y)


#****************************************************************
#****************************************************************
# Slicing string - not included
#****************************************************************
#****************************************************************
b = "Hello, World!"
print(b[2:5])  #llo print position 2 to position 5 (not included)
print(b[:5]) #Hello
print(b[2:]) #llo, World!

#****************************************************************
#****************************************************************
# Update string
#****************************************************************
#****************************************************************
#uppercase
a = "Hello, World!"
print(a.upper())

#lowercase
a = "Hello, World!"
print(a.lower())

#trim (remove back and front space)
a = " Hello, World! "
b = a.strip() # returns "Hello, World!"

#left trim
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.as") #return ww.....banana

#right trim
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qw") # return banana,,,,,ss


#replace string - case sensitive
a = "Hello, WOrld!"
print(a.replace("o", "K")) #return "HellK, WOrld"

#replace string - with occurence
txt = "one one was was one too."
x = txt.replace("one", "three", 2)
print(x) #return "three three was was one too."

#explode
a = "Hello, World!"
b = a.split(",")
print(b) # returns ['Hello', ' World!'] list

#implode
. = ("John", "Peter", "Vicky")
x = ",".join(myTuple)
print(x) #return "John,Peter,Vicky"

# implode dictionary 
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x) #return nameTESTcountry means only key is joined

#concate string
a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld

# concate variable in string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# count occurence of word count("search word", start position)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# find first occurence position
txt = "Hello, welcome to my world."
x = txt.find("we", 5, 10) #if have will return position if not will return -1
y = txt.index("q") #will return position if not will return exception

# find first occurence position from back
txt = "Mi casa, su casa."
x = txt.rfind("casa") #will return 12 the first c from back
y = txt.rindex("q") #will return position, if not return exception



# check alphanumeric 
# alphabet letter (a-z) and numbers (0-9).
# not alphanumeric: (space)!#%&? etc.
txt = "Company12"
x = txt.isalnum()
print(x) #will return true but if Company 12 then will return false


# check alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)

# check number (not decimal)
txt = "508.00"
x = txt.isdigit()
print(x) #will return False

txt = "565543"
x = txt.isnumeric() #same as above
print(x)


#format 2 decimal place
price = 49
txt = "{:.2f}"
x = txt.format(price)
print(x)






#****************************************************************
#****************************************************************
# IF ELSE
#****************************************************************
#****************************************************************
if 5 > 2:
  print("Five is greater than two!")

#-------------------------------------
#if in string (return True OR False)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#-------------------------------------
#if not in string (return True OR False)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#-------------------------------------
#else if
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


a = 200
b = 33
c = 500
#-------------------------------------
#with and condition
if (a > b) and (c > a):
  print("Both conditions are True")

#-------------------------------------
#with or condition
if (a > b) or (a > c):
  print("At least one of the conditions is True")

#-------------------------------------
#reverse result (not...!)
if not a > b:
  print("a is NOT greater than b")



#****************************************************************
#****************************************************************
# For loop
#****************************************************************
#****************************************************************
# loop in a string
for x in "banana":
  print(x) #return b a n a n a

#----------------------------------------------
# loop in array/list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# loop in array/list (via index)
for i in range(len(thislist)):
  print(thislist[i])


#----------------------------------------------
# loop in a dictionary/associative array 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# loop in dictionary - print only keys
# "brand" "model" "year"
for x in thisdict:
  print(x) 
#or
for x in thisdict.keys():
  print(x)


# loop in dictionary - print only values
#"Ford" "Mustang" 1964
for x in thisdict:
  print(thisdict[x]) 
#or
for x in thisdict.values():
  print(x)

# loop in dictionary - print both
for x, y in thisdict.items():
  key = x
  value = y

#----------------------------------------------
# break in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#----------------------------------------------
# continue
# stop current iteration and move to next iteration (skip action)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#-----------------------------------------------
# for range
# default start with 0
# end not included
for x in range(6):
  print(x) #print 0 1 2 3 4 5

# with start value
for x in range(2, 6):
  print(x) #print 2 3 4 5

# with increment set
# increase by 3
for x in range(2, 30, 3):
  print(x) #print 2 5 8 11..........

#-------------------------------------------------
# for else
# action to be done once condition no longer true
#if break else will not execute
for x in range(6):
  print(x)
else:
  print("Finally finished!")






#****************************************************************
#****************************************************************
# While loop
#****************************************************************
#****************************************************************
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i]) #return "apple"  "banana"  "cherry"
  i = i + 1 
#-------------------------------------------------
#break in while loop
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break #will only print 1 2 3
  i += 1

#-------------------------------------------------
# continue
# stop current iteration and move to next iteration (skip action)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#-------------------------------------------------
# while else
# action to be done once condition no longer true
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#****************************************************************
#****************************************************************
# Length
#****************************************************************
#****************************************************************
a = "Hello, World!"
print(len(a)) #13


#****************************************************************
#****************************************************************
#GLOBAL VARIABLE
#****************************************************************
#****************************************************************
# Can be used for inside and outside Function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)  #will print fantastic

myfunc()

print("Python is " + x) #will print awesome

#----------------------------------------------------------------
# Overwriting a global variable in function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#****************************************************************
#****************************************************************
#Calculation Operator 
#****************************************************************
#****************************************************************
x = 6
y = 3

a = x + y #return 9
b = x - y #return 3
c = x * y #return 18
d = x / y #return 2.0

#modules (find remainders)
x = 8
y = 3

e = x % y #return 2 (3x2=6 left 2 to 8)

#exponential
x = 3
y = 2
z = x ** y #return 3*3 = 9

#floor division
#rounds the result down to the nearest whole number
x = 15
y = 2

z = x // y #return 7

#****************************************************************
#****************************************************************
#Assignment Operator 
#****************************************************************
#****************************************************************
x += 3 # x = x + 3

x -= 3 # x = x - 3

#... any operation above plus = will be x = x _ 3


#****************************************************************
#****************************************************************
#Compare Operator 
#****************************************************************
#****************************************************************
x = 3
y = 2

# x == y  equal
# x != y  not equal
# x > y   greater than
# x < y   lesser than
# x >= y  greater than or equal to
# x <= y  lesser than or equal to


#****************************************************************
#****************************************************************
#logical Operator 
#****************************************************************
#****************************************************************
x = 8

# x > 5 and x < 10        ----both true then true
# x > 5 or x > 10          ----one true then true
# not(x > 3 and x < 10)   ----both true return false 

#****************************************************************
#****************************************************************
#membership Operator 
#****************************************************************
#****************************************************************
x = ["apple", "banana"]

print("banana" in x) #return true
print("banana" not in x) #return false as there is banana

#****************************************************************
#****************************************************************
#List Function
#****************************************************************
#****************************************************************
#same as array();
#start with 0

#construct new array
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) #return ["apple", "banana", "cherry"]

#array count()
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #return 3

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#search by index
print(thislist[1]) #return "banana"

#search by word (find position)
thislist.index('MSFT')

#extract by range
print(thislist[2:5]) #return ["cherry", "orange","kiwi"] position 5 not included

#if in array
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #return True

#replace value in array by index
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #return ["apple", "blackcurrant","cherry"]

#add value in array with position indicated
thislist.insert(2, "watermelon") 
print(thislist) #return ["apple", "blackcurrant","watermelon","cherry"]


#add value in array arraypush();
thislist.append("orange")
print(thislist) #return ["apple", "blackcurrant","watermelon","cherry", "orange"]

#append a list to another list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #return ["apple", "blackcurrant","watermelon","cherry", "orange","mango", "pineapple", "papaya"]

#remove from exact word
tropical = ["mango", "pineapple", "papaya"]
tropical.remove("pineapple")
print(thislist) # return ["mango", "papaya"]


#remove by index
#default remove last item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #return ["apple", "cherry"]

#sort list
thislist.sort() #default in ascending order a,b,c  1,2,3 case sensitive 
thislist.sort(reverse = True) #descending order c,b,a  3,2,1

#sort list (non case sensitive)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

#customize sort list
#find the number nearest to 50 - smallest number will return first
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#reverse the whole list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #return ["cherry", "Kiwi", "Orange", "banana"]

#return only unique value in list
def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

#****************************************************************
#****************************************************************
#Dictionaries Function
#****************************************************************
#****************************************************************
#associative array
#construct dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
#or
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#or 
thisdict = {}

x = thisdict["brand"] #ford associative array

#duplicate key will be replace by the one after
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict["year"]) #2020

#dictionary length
y = len(thisdict)

#get list of keys 
x = thisdict.keys() # return ["brand","model","year"]

#get list of values
x = thisdict.values()

#add pair
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["color"] = "white" #add "color": "white"
car["year"] = 2020 #overwrite "year": 2020
thisdict.pop("model") #remove model pair
thisdict.popitem()#remove last pair


#if key exist
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
  print("Yes")

#access nested value
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
}

print(myfamily["child2"]["name"]) #return "Tobias"

#****************************************************************
#****************************************************************
#Function
#****************************************************************
#****************************************************************

#create function
def my_function():
  print("Hello from a function")

my_function() #call the function above

#pass in values
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#set default function
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India") #print "I am from India"
my_function() #print "I am from Norway"

#return value
def my_function(x):
  return 5 * x

print(my_function(3)) #print 8




#****************************************************************
#****************************************************************
#Set Function
#****************************************************************
#****************************************************************
#unordered, unchangable, distinct list no repeated values
#the set is random order 

#construct set
thisset = set(("apple", "banana", "cherry"))

thisset = {"apple", "banana", "cherry", 1, True, 2, "cherry"}
print(thisset) #will return {"apple", "banana","cherry",1, 2} as True and 1 is the same it will return the first one
print(len(thisset)) #return 5 (count distinct)

#add to set
thisset.add("orange")

#concate set with set/list
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

thisset.update(tropical)
thisset.update(mylist) #can concate with list
set3 = thisset.union(tropical) #for create new set

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #will cause error if item doesn't exist
thisset.discard("banana") #will not caused error if item doesn't exist


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #return {"apple"}.....only keep duplicate (update to x)
x.symmetric_difference_update(y) #return {"banana","cherry","google","microsoft"}.....other than duplicate keep the rest (update to x)

z = x.intersection(y) #return {"apple"}.....only keep duplicate (create new set)
z = x.symmetric_difference(y) #return {"banana","cherry","google","microsoft"}.....other than duplicate keep the rest (create new set)

#****************************************************************
#****************************************************************
#class and object
#****************************************************************
#****************************************************************
#Simple class and function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) #print John
print(p1.age) #print 36

#define how will the info return using __str__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} {self.age}"    

p1 = Person("John", 36)

print(p1)

#object can be a function to be called.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    return "Hello my name is " + self.name

p1 = Person("John", 36)
x = p1.myfunc()
print(x) #it will print Hello my name is John

#modify object
p1.age = 40 #now age will be 40 instead of 36

#-----------------------------------------------
#Inheritance (parent and child class)

#parent class like normal class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#child class 
class Student(Person):
  def __init__(self, fname, lname, year): #if content is different it will overwrite parent object
    super().__init__(fname, lname) #inherit Person object and functions
    self.graduationyear = year #added parameter

  def welcome(self): #added function
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019) #using child class to assign 
x.welcome() #use child class function

#****************************************************************
#****************************************************************
#Import Function
#****************************************************************
#****************************************************************
#Create own function
#on one file save this name mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

def greeting(name):
  print("Hello, " + name)

#on another file import mymodule.py things
import test as mx
a = mx.person1["age"]
print(a) #print 36 

x = mx.greeting("JJ")
print(x)

#--------------------------------------------
#if only import 1 using "from" 
# item then can use directly
from test import person1
print (person1["age"])

#--------------------------------------------
#generate random number
import random
print(random.randrange(1, 10));

#--------------------------------------------
#check Operating System
import platform

x = platform.system()
print(x)

#--------------------------------------------
#get curent datetime
import datetime

x = datetime.datetime.now()
print(x) #2023-03-18 19:59:48.586547
print(x.strftime("%d")) #Day of the month (18)

print(x.strftime("%b")) #Month short(Mar)
print(x.strftime("%B")) #Month(March)
print(x.strftime("%m")) #Month number(03)

print(x.strftime("%y")) #Year short(23)
print(x.strftime("%Y")) #Year short(2023)

print(x.strftime("%H")) #24 Hour(19)
print(x.strftime("%I")) #12 Hour(07)
print(x.strftime("%p")) #AM/PM(PM)

print(x.strftime("%M")) #Minutes (59)
print(x.strftime("%S")) #Minutes (59)

print(x.strftime("%d")) #Day of the month (18)
print(x.strftime("%d")) #Day of the month (18)
print(x.strftime("%a")) #Sat
print(x.strftime("%A")) #Saturday
print(x.strftime("%w")) #if is Saturday then 6


#--------------------------------------------
#create own datetime
import datetime
x = datetime.datetime(2020, 5, 17)

#--------------------------------------------
#build in maths
x = min(5, 10, 25) 
y = max(5, 10, 25)

x = abs(-7.25) #absolute positive return 7.25
x = pow(4, 3) #power, 4 to the power of 3 - 4*4*4

#-------------------------------------------
#math funtion (extra)
import math
x = math.sqrt(64) #square root - 8.0
x = math.ceil(1.4) #round up - 2
y = math.floor(1.4) #round down - 1
x = math.pi #3.14159

#-------------------------------------------
#json
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#convert python dic to json 
y = json.dumps(x) 

#print pretty json
y = json.dumps(x)

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

#****************************************************************
#****************************************************************
#useful function
#****************************************************************
#****************************************************************
#Given a string of lowercase letters, make the string smallest in lexicographical order by swapping its characters.
x = ['132', '100', '764', '514', '282', '354', '293', '241'] #order


#Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
#the smallest in lexicographical order
#among all possible results.

#Input: s = "bcabc"
#Output: "abc"

#Input: s = "cbacdcbc"
#Output: "acdb"


#Sort numbers based on prime factorization.
#Input: N = 5, Numbers = [3, 4, 8, 9, 12]
#Output: 4, 8, 12, 3, 9
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

#Write a program which determines whether a snake (in the game Snake) wins the game or ends up eating itself
#4L,4R,3U,3D
#basic recursive function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6) #print 1 3 6 10 15 21

#****************************************************************
#****************************************************************
#error handling
#****************************************************************
#****************************************************************
try:
  print(x) #your test code
except NameError:
  print("Variable x is not defined") #specify handle error
except:
  print("An exception occurred") #if error print this
else:
  print("Nothing went wrong") #when nothing happen 
finally:
  print("The 'try except' is finished") #action taken no matter pass or failed

#------------------------------------------
#when open file that cannot be written. It will close object no matter
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#check type raise error
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")


