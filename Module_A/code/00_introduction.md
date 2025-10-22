---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

Check online documentation on jupyter [here](http://nbviewer.jupyter.org/urls/bitbucket.org/ipre/calico/raw/master/notebooks/Documentation/Reference%20Guide/Reference%20Guide.ipynb)

```python
print("this is python, programming is fun again")
```

## Variables

```python
# This b.t.w is a comment

variable = 2
```
```python

print(variable)
type(variable)


```

the function `print` allows also more powerful way of outputting numbers:

```python
print("Art: %5d, Price per unit: %8.2f"% (453, 59.058))
```

```python
a, b = 5, "1" # a python trick to assign values to more than one variable
print(a,b)
a+b
```

try to sum a and b; if it doesn't work, cast one of the two and repeat

```python
x = y = z = 7 # multiple assignment
print(x, y, z)
```

```python
y=5
```

```python
print(x, y, z)
```

what if you reassign one of the three (say $y$)?

```python
# can set values from command line as well (rarely used)
x = input("set the value of x")
print(x)
```

<!-- #region -->
### Pointers in Python? 


Pointers are widely used in C and C++. Essentially, they are variables that hold the memory address of another variable.  Are there pointers in python? Essentially no.
Pointers go against the [Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3):

*Pointers encourage implicit changes rather than explicit. Often, they are complex instead of simple, especially for beginners. Even worse, they beg for ways to shoot yourself in the foot, or do something really dangerous like read from a section of memory you were not supposed to. Python tends to try to abstract away implementation details like memory addresses from its users. Python often focuses on usability instead of speed. As a result, pointers in Python doesn’t really make sense.*


It's all about two basics python concepts:
1. Mutable vs Immutable objects
2. Variable/Name in python

Mutable objects can be changed, immutable cannot. I.e. when a new value is assigned to a given immutable "variable", a new object is in reality created. This as "variable" in python are actually just names bound to objects (PyObject).

For more details about all this refer e.g. to [this review](https://realpython.com/pointers-in-python/)
<!-- #endregion -->

## Operators
the usual stuff..

```python
print(3 / 4)
print(3.0 / 4.0)
print(3 % 4)
print(3 // 4)
print(3**4)
print(pow(3, 4))

x = 1
print(type(x))
y = 1.0
print(type(y))
#a,b = int(3), int(4)
#print(a / b)
#print(float(a) / float(b))
```

## Iterators
very similar to all other languages. Start exploring the `range` and `enumerate` functions

```python
for i in [1,2,3,4,5,6,7,8,9]: print (i)
```

```python
i = 1
while i < 10:
    print(i)
    i+=1
```

```python
for i, j in enumerate(["a","b","c"]): print(i,j)
```

## Conditional Statements
Mind the indentation! 

```python
a = 22
if a >= 22: 
    print("if")
    if a==3: 
        print(3)
    elif a >= 21:
        print("elif")
else:
    if 7>5: print ("of course")
    print("else")
```

try/except: a very important and powerful type of conditional expression, use it and use it with care 

```python
a = "1"
try:
    b = a + 2
    print (b)
except:
    print(a, " is not a number")
```

```python
my_function(10)
```

# Functions

```python
def my_function(a, b = 2):
    result = a + 2 * b
    return result

my_function(1)
```

Notice that the function does not specify the types of the arguments, like you would see in statically typed languages. This is both useful and dangerous. Use the try/except construction to make it safe


function can edit "global" variables as well, i.e. variables that are declared outside the function scope. To do so the statement ```global``` is used

```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

```python
x = "awesome"

def myfunc():
  global x 
  x = "fantastic"

myfunc()

print("Python is " + x)
```

# Lists, Tuples, Dictionaries


## Lists
Lists are exactly as the name implies. They are lists of objects. The objects can be any data type (including lists), and it is allowed to mix data types. In this way they are much more flexible than arrays. It is possible to append, delete, insert and count elements and to sort, reverse, etc. the list.

```python
a_list = [1, 2, 3, "this is a string", 5.3]
b_list = ["A", "B", "F", "G", "d", "x", "c", a_list, 3]
print(b_list)
```

Manipulations of list is rather intuitive:

`list[start:stop:step]`

```python
a = [7, 5, 3, 4, 10]
print(a[0])
print(a[-1])
print(a[2:4])
print(a[:3])
print(a[3:])
print(a[-3:])
print(a[3:len(a)])
print(a[1::3])
```

Operations on lists are also straightforward. Note that some of them do not modify the list permanently.

```python
a.insert(0, 0) # position, value
print(a)
a.append(8)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)
a.remove(3) # value
print(a)
a.remove(a[4])
print(a)
```

Very fancy operations are possibile (known as list [comprehensions](https://docs.python.org/2/tutorial/datastructures.html?highlight=comprehensions))

```python
even_numbers = [x**2 for x in range(20) if x % 2 == 0]
print(even_numbers)
```

strings are lists and feature all operations permitted on lists, comprehensions as well

```python
first_sentence = "It was a dark and stormy night."
characters = [x for x in first_sentence]
print(characters)
```

the opposite is also possible, but in a different way:

```python
second_sentence = ''.join(characters)
print(second_sentence)
```

### Strings and String Handling
One of the most important features of Python is its powerful and easy handling of strings. Defining strings is simple enough in most languages. But in Python, it is easy to search and replace, convert cases, concatenate, or access elements. We’ll discuss a few of these here. For a complete list, see this [tutorial]( http://www.tutorialspoint.com/python/python_strings.htm)

```python
a = "A string of characters, with newline \n CAPITALS, etc."
print(a)
b = 5.0
newstring = a + "\n We can format strings for printing %.2f"
print(newstring % b)
```

Operations are easy (remember strings are lists!)

```python
a = "ABC DEFG"
print(a[1:3])
print(a[0:5])
```

```python
a = "ABC defg"
print(a.lower())
print(a.upper())
print(a.find('d'))
print(a.replace('de', 'a'))
print(a)
b = a.replace('def', 'aaa')
print(b)
b = b.replace('a', 'c')
print(b)
b.count('c')
```

```python
print("ABC defg".lower())
```

## Tuples
Tuples are like lists with one very important difference. Tuples are not changeable.

```python
a = (1, 2, 3, 4)
print(a)
a[1] = 2
```

## Dictionaries
Dictionaries are of paramount importance and a major asset of python.
They are unordered, keyed lists. Lists are ordered, and the index may be viewed as a key.

```python
a = {'anItem' : "A", 'anotherItem' : ["a,bc"], 3 : "C", 'afourthItem' : 7} # dictionary example
print(a['anItem'])
```

```python
for i in a: print(i, a[i])
```

```python
print("Keys:", a.keys())
print("Values:", a.values())
```

## Sets


Sets are used to store multiple items in a single variable, but differently from lists and dictionaries, they are unordered and do not support duplicates.
In addition you cannot access items in a set by referring to an index or a key, but you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

```python
a = {"apple", 2, "cherry", 2}
print(a)
```

```python
print(a[1])
```

```python
for i in a: print(i)
```

```python
a.add("3")
print(a)
a.update({7, "banana"})
print(a)
```

```python

```
