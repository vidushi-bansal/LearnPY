# Python Basics  
General purpose programming language  
Used for:  
1. Web application  
2. Machine Learning  
3. Automation  
and many more  
  
## Core Data Types in Python  
### Int (Integer)  
123  
-10   
-123123  
3342535  
  
### Float (Decimal Number)  
1.0  
2.421  
-21.42  
  
### String (Anything surrounded by '' or ""  | Sequence of characters and numbers)  
'hello'   
"hello"  
'123'  
'Hi "Vidushi"'  
'23.53'  
  
### Bool (One of 2 values | True/False | 1/0)
True  
False  
  
## Output and Printing  
### Print (Output data to the console)  
print('Hello there!')  
print(43.5)  
print(23.35, "Hello", True, end='\n')   
#### Default end='\n'  
  
## Variable  
This is used for storing data.  
  
hello = 'tim'  
world = hello  
print(hello, world)   -> tim tim  
  
## Input a value  
Taking user input from console  
  
input('Name: ')    -> Name: Vidushi  
  
#### Storing the input to a variable  
name = input('Name: ')  
age = input('Age: ')  
print('Hello', name, '. You're', age, 'years old!')  
  
## Arithmetic Operators  
Operands should be of same data types and numbers.  
  
Division operator always gives a float number  
div = 9/3            -> 3.0  
res = 10//3          -> 3  (Integer result of division, removes all decimal points)  
mod = 10/3           -> 1 (Remainder)  
  
  
a = input('a= ')    -> It takes string value as input  
b = input('b= ')  
  
x = 1 + a                 -> Error   
y = 1 + int(b)            -> Correct  
  
## Methods    
hello = 'hello'   
print(type(hello))                     -> <class> str  
print(hello.upper())                   -> HELLO  
print(hello.capitalize())              -> Hello  
print(hello.lower().count('ll'))       -> 1  
  
  
## Printing strings multiple times (Concat)  
**Example**  
x = 'hello'  
y = 3  
print(x * y)         -> hello hello hello  

## Conditional Operators  
Compares 2 values or datatypes and gives result as:  
True  
False  
  
Operators are as follows:   
== Equal to  
!= Inequality   
<= Less than or equal to  
>= Greater than or equal to  
<  Less than  
>  Greater than  
  
x = "hello"  
y = 'hello'  
print(x == y)        -> True  
  
print('a' > 'Z')     -> True  (ASCII Code value comparison)  
  
##### Print the ordinal value of a character  
print(ord('Z'))            -> 90  
print(ord('a'))            -> 97  
  
Therefore, 'a' > 'Z'  

## IF-ELSE-ELIF
if condition:  
  <>  
elif condition:  
  <>   
else:  
  <>  
    
**Example**  
x = input('Name: ')  
if x == 'Tim':  
  print("Hey Tim!")  
  print()  
elif x == 'Joe'  
  print("Hey Joe!")  
elif x == 'Maddy'  
  print("Hey Maddy")  
else:  
  print("Who are you?")  
print("How are you?")  
  
======================================================================================================  
## Collections  
An unordered or ordered group of elements    
  
### **1. List**
> A list of elements. Elements are some data types and they need not to be the same.  
> A list can store a bunch of different elements.  
> It is an ordered collection, which means the order in which we enter things into the collection matters and is maintained.  
> List are mutable, which means that the variable stores the reference to the list instead of copy, and actual items are stored elsewhere  
> The elements of the list can be changed.  
x = [4, True, "Hello"]  
  
#### Accessing elements in the list  
x = []             -> Empty list    
x = [4, True, "Hello"]    
num = x[0]         -> num is the 1st element of the list   
  
#### Functions of the list  
##### Length of the list  
length = len(list)      -> Gives 3  
##### Append things to the list  
Add to the end of the list  
x.append('hi')  
print(x)            -> [4, True, "Hello", 'hi']  
##### Extend the list  
x.extend([1,23,'hi','end'])  
print(x)            -> [4, True, "Hello", 'hi', 1, 23, 'hi', 'end']  
##### Removing/Popping elements out of the list  
x.pop()            -> Removes the last element from the list  
print(x.pop())     -> Removes 'end' from the list and prints it  
  
If we want to remove an element from a particular index  
x.pop(0)             -> Removes the 1st element  
##### Changing the element at a particular index  
x = [4, True, "Hello"]  
x[2] = 'time'  
print(x)                  -> [4, True, "time"]  
##### List of list of list of ..  
x = [[],(), [[[], [], 2], True, ["ABC", 56]]]  
##### Mutability of the List  
x = [4, True, "Hello"]  
y = x                -> y points to the same place as x  
y[0] = 10  
print(y)             -> [10, True, "Hello"]  
print(x)             -> [10, True, "Hello"]    -> x is pointing to the same location as y.  
  
So, in order to retain the value of x.  
x = [4, True, "Hello"]  
y = x[:]                -> y creates a copy of x  
y[0] = 10  
print(y)  
print(x)  

### **2. Tuples**  
Similar to list, but they are immutable.   
List uses [], tuples uses ()  
x = (1,True,"Hi")  
We cannot append, remove or change the elements in the tuple once its defined.  
If we do need to change it, then we have to redefine it.  
##### Print elements from tuple    
print(x[0])        -> 1  
===========================================================================================  

### For Loops  
Allows us to iterate to a set number of times  
While loop runs indefinite amount of time based on a condition.  
We know how many times to iterate in For loop  
  
##### Snippet
for i in range(5):  
  print(i)                -> 0 1 2 3 4  
  
range(start, stop, step)  
If we only pass 1 argument, that is the stop element. It will automatically start from 0  

for i in range(0):  
print(i)                -> Prints nothing  
  
  
for i in range(1,5):  
print(i)                ->  1 2 3 4  
  

for i in range(1,5,2):  
  print(i)              -> 1 3  
  

##### Using For loop to print elements of the list  
for i in [32,12,"Hello",39,False]:  
  print(i)             -> 32 12 Hello 39 False  
  
x = [32,12,"Hello",39,False]  
for i in range(len(x)):   
print(x[i])           -> 32 12 Hello 39 False  
  
for i, element in enumerate(x):  
  print(i, element)  
  
Output:  
0 32  
1 12  
2 Hello  
3 39  
4 False  
  
=====================================================================================
### While Loops
While condition == True:  
  do something  

i = 0  
while i < 5:  
  print('Hi')      Hi Hi Hi Hi Hi   
  i+=1  

The above logic can also be written as:  

i = 0  
while True:  
  print('Hi')      Hi Hi Hi Hi Hi  
  i+=1  
  if i == 5:  
     break  
  
============================================================================================  
### Operators  
#### Slice Operator  
Take a slice or a part of a collection(list, tuple) or a string  
  
x = (1,2,3,4,5,6,7,8)  
y = ['hi', "there", True, 13, 15, "Line"]  
s = "vidushibansal"  

sliced = [start:stop:step]  
sliced = x[0:5:2]    -> (1 , 3, 5)  
sliced = x[4:0:-1]    -> (5, 4, 3, 2)  
sliced = x[4::-1]     -> (5, 4, 3, 2, 1)  
sliced = y[0:5:2]    -> ['hi', True, 15]  
sliced = y[:2]       -> ['hi', 'there']              -> Start from 0 to 2  
sliced = y[2:]       -> [True, 13, 15, 'Line']       -> Start from 2 till end  

  
To reverse a list  
sliced = x[::-1]    -> (8, 7, 6, 5, 4, 3, 2, 1)  
sliced = s[::-1]    -> lasnabihsudiv  
print(sliced)        
 
======================================================================================  
### Sets
Very useful datatypes in python  
It is an unordered unique collection of elements  
There are no duplicate elements  
There is no notion of position as we have in list  
Is used to see if something exist or !exist   
Its not used to check the frequency or order of any element  
  
x = set()                -> To create an empty set  
s = {4,56,23,12, 12}     -> To create a set with elements  
print(s)                 -> {56, 4, 12, 23}  -> Removes duplicate value and print elements in any order  
#### Add elements to a set  
s.add(32)             -> Only adds one element at a time  

#### Remove elements from a set  
s.remove(4)  
  
#### To check if something is in a set
print(23 in s)          -> True  

#### Union of 2 sets  
s1 = {1,2,3,4}  
s2 = {4, 5,6,7,8}  
print(s1.union(s2))         -> {1, 2, 3, 4, 5, 6, 7, 8}   
print(s1.difference(s2))    -> {1, 2, 3}  
print(s1.intersection(s2))  -> {4}   
 
======================================================================================  
### Dictionaries  
It is similar to a hash table or a map  
A key-value pair  

x = {'key' : [1,32]}  
print(x['key'])         -> [1,32]  
x['key1']=6  
print(x)                -> {'key': [1, 32], 'key1': 6}  
x[4]="Hello"  
print(x)                -> {'key': [1, 32], 'key1': 6, 4: 'Hello'}  
  
#### To check for any key in the dictionary
x = {'key' : 3}  
print('key' in x)       -> True  
  
#### Get all the values from the dictionary
x = {'key': [1, 32], 'key1': 6, 4: 'Hello'}  
print(x.values())       -> dict_values([[1, 32], 6, 'Hello'])  
print(x.keys())         -> dict_keys(['key', 'key1', 4])  
print(list(x.values())) -> [[1, 32], 6, 'Hello']  
print(list(x.keys()))   -> ['key', 'key1', 4]  
  
#### Deleting values  
del x['key']  
print(list(x.keys()))   -> ['key1', 4]  

#### To loop over a dictionary  
for key, value in x.items():             -> key [1, 32] /n key1 6 /n 4 Hello  
  print(key, value)  

This can also be written as:  
  
for key in x:  
  print(key,x[key])  
  
========================================================================================  
### Comprehensions  
One line initialization of a list, tuple, dictionary, etc  
  
#### Examples:  
**1. List**   
x = [x for x in range(5)]  
     |  
     Element to add to the list  

print(x)                       -> [0,1,2,3,4]  
  
x = [x + 5 for x in range(5)]  
print(x)                       -> [5,6,7,8,9]  
  
x = [x % 2 for x in range(5)]  
print(x)                       ->[0,1,0,1,0]   
    
x = [0 for x in range(5)]   
print(x)                       -> [0, 0, 0, 0, 0]  
  
  
x = [[0 for x in range(3)] for x in range(5)]  
print(x)                       -> [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  
  
x = [i for i in range(50) if i % 5 == 0]  
print(x)                       -> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]  
  
**2. Dictionary**  
  
x = {i:0 for i in range(10) if i % 5 == 0}  
print(x)                         -> {0: 0, 5: 0}  
   
x = {'key':i for i in range(50) if i % 5 == 0}  
print(x)                       -> {'key': 45}  
  
**3. Set**  
x = {i for i in range(10) if i % 5 == 0}  
print(x)                        -> {0, 5}  
  
**4. Tuples**
x = tuple(i for i in range(10) if i % 5 == 0)  
print(x)                        -> (0, 5)  
  
========================================================================================  
### Functions
Functions are objects. You can return a value.  
They can have arguments  
##### To define a function use def keyword  
**Example 1**  
def func():  
  print("Hello")  
func()  

**Example 2**  
def func():  
  print("Function1")  
  def func():  
    print("Insider function")  
  func()    
  
func()  
  
Output:  
Function1  
Insider function  
  
**Example 3**  
def func(x,y):  
  print("Values are:", x, y)  
func(2,4)                            -> Values are: 2 4  
  
**Example 4**  
def func(x,y):   
  return x + y  
sum = func(2,4)   
print("Sum of 2 numbers are:",sum)                       ->Sum of 2 numbers are: 6  
  
print("Values are:", x, y)  
  
**Example 5**  

def func(x,y):   
  return x + y, x * y  
sum,mul = func(2,4)  
print("Sum of 2 numbers are:",sum)  
print("Multiplication of 2 numbers is:",mul)  
  
Output:  
Sum of 2 numbers are: 6  
Multiplication of 2 numbers is: 8  
  
**Example 6**
def func(x,y,z=None):                  -> z is an optional value, you don't necessarily have to pass it  
  return x + y, x * y  
sum,mul = func(2,4)  
print("Sum of 2 numbers are:",sum)  
print("Multiplication of 2 numbers is:",mul)  
  
=======================================================================================  
### Unpack Operator  
  
**Example 1**  
def func(x):  
  def func2():  
    print(x)  
  return func2()  
  
print(func(2)())  
  
**Example 2**  
def func(x):  
  def func2():  
    print(x)  
  return func2()  
  
x= func(2)  
x()   
  
=================================================================================  
### *args and **kwargs  
Unpack operator separates all elements from the list/collection into individual elements  
  
x = [1,235, 43, 234]    
print(x)                    -> [1, 235, 43, 234]   
print(*x)                   -> 1 235 43 234           ->> unpack and sends it through as arguments  

def func(x,y):  
  print(x,y)  

pairs = [(1,2),(3,4)]  
for pair in pairs:  
  func(*pair)  
  
Output:  
1 2  
3 4  

We can do it with dictionaries as well.  
**Example**  
def func(x,y):  
  print(x,y)  
func(**{'x':2, 'y':5})                    -> 2 5  
   
If we have a function nd we don't know how many arguments: positional or keywords that we want to accept.  
kwargs stands for keyword arguments.  
  
**Example**  
def func(*args, **kwargs):  
  print(args,kwargs)  
  
func(1,2,3,4,5,one=1, two=2)                   -> (1, 2, 3, 4, 5) {'one': 1, 'two': 2}  
   
**Example**  
def func(*args, **kwargs):  
  print(*args,*kwargs)  
   
func(1,2,3,4,5,one=1, two=2)                 -> 1 2 3 4 5 one two  
  
**Example**  
def func(*a, **k):  
  print(*a,*k)  
  
func(1,2,3,4,5,one=1, two=2)  
  
==============================================================================================  
### Scopes and Global  
  
#### Local  
**Example**  
x = 'tim'  
  
def func(name):  
  x = name  
print(x)  
func('changed')  
print(x)                                  -> tim tim  
  
x will not change because it was only changed locally, i.e, inside the function.  
  
#### Using global keyword  
**Example**  
  
x = 'tim'  
  
def func(name):  
  global x                           -> tells that x should be global  
  x = name  
print(x)  
func('changed')  
print(x)                            -> tim changed  
    
=========================================================================================  
  
### Exceptions in Python  

#### Raise Exceptions:  
There is a keyword called raise.  
  
raise Exception('Incorrect')  
raise FileExistError('')  
  
#### Handle Exceptions  
We have a try except finally block in Python  
  
**Example**  
try:   
  x = 7/0  
except Exception as e:  
  print(e)  
  
**Example**  
try:  
  x = 7/0  
except Exception as e:  
  print(e)  
finally:  
  print("Final Output")  
  
=========================================================================================  
### Lambdas  
A lambda is a one line anonymous function. Its not a named function.  
We don't define a lambda using a def keyword.  
  
**Example**  
a = lambda x: x + 5  
print(a(2))                    -> 7  
This lambda is going to take one argument which is x and it will return x+5  
Consider this as a funcion called a which takes x as an argument and return whatsoever is after :  
**Example**  
a = lambda x,y: x+y  
print(a(5,6))  
  
==========================================================================================  
### Map & Filter    
Two useful functions in Python that makes use of the lambda functions  
  
#### Map  
**Example**  
x = [1,2,3,4,5,6,7,8,121,235,463,34,23,235,6,23]  
mp = map(lambda i: i+2, x)  
print(list(mp))                                   -> [3, 4, 5, 6, 7, 8, 9, 10, 123, 237, 465, 36, 25, 237, 8, 25]  
We are going to map all elements of x. Take this lambda function and apply it on every single  
element of x and then put it into a new list.  
  
#### Filter  
Filters out on the basis of condition  
**Example with lambda**  
x = [1,2,3,4,5,6,7,8,121,235,463,34,23,235,6,23]  
mp = filter(lambda i: i % 2 == 0, x)  
print(list(mp))                                  -> [2, 4, 6, 8, 34, 6]  
  
**Example without lambda**  
x = [1,2,3,4,5,6,7,8,121,235,463,34,23,235,6,23]  
def func(i):  
  return i % 2 == 0  
  
mp = filter(func, x)  
print(list(mp))                         -> [2, 4, 6, 8, 34, 6]  
  
========================================================================================  
### F Strings  
tim = 90  
x = f'name {6 + 8} {tim}'  
print(x)                            -> name 14 90  
  
=========================================================================================  

























