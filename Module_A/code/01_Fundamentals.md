---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: Python [conda env:base] *
    language: python
    name: conda-base-py
---

# Modules/packages/libraries

Definitions:

  * Modules:
  A module is a file which contains python functions, global variables etc. It is nothing but .py file which has python executable code / statement.

  * Packages:
  A package is a namespace which contains multiple package/modules. It is a directory which contains a special file `__init__.py`
  
  * Libraries:
  A library is a collection of various packages. There is no difference between package and python library conceptually.
  
Modules/packages/libraries can be easily "imported" and made functional in your python code. A set of libriaries comes with every python installation. Others can be installed locally and then imported. Your own code sitting somewhere else in your local computer can be imported too.

Further details (very important!) on packages and how to create them can be found online. We may find the need of creating our own during the course.

```python
###### all the "stuff" that is in the math library can be used
import math
print(math.pi)

# you can give math a label for convenience
import math as m
print (m.pi)

# alternatively you can import only a given "thing" from the library
from math import pi    #you can add several libraries at once, just list them separated by a ", "
print (pi)

# or just get everything (very dangerous!!!)
#from math import *
#print (sqrt(7))
```

To know which modules are there for you to use just type:

```python
print (help('modules') )

```

`pip` is a special package. It is used from the command line to install properly (e.g. matching the version of the local packages) new packages. It can also be used from within python to check i.e. the set installed packages and their versions. N.B.: only the installed packages on top of the default ones will be listed 

```python
"""""
try:
    # this doesn't work anymore
    import pip
    sorted(["%s==%s" % (i.key, i.version) for i in pip._internal.utils.misc.get_installed_distributions()])
    print ("within try")
""""" 
# use this instead
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    for i in installed_packages])
print(installed_packages_list)

```

# Copies and Views

#### Copies:
* A **copy** creates a new object that is a duplicate of the original one.
* Changes made to the copy do not affect the original object, and vice versa.
* There are two types of copies:
  * Shallow Copy: Only the top-level object is copied. If the original object contains references to other objects (e.g., a list of lists), the references are copied, not the objects themselves.
  * Deep Copy: A complete copy is made, including all nested objects. Changes to any part of the deep copy won’t affect the original object.

```python
import copy
original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)

shallow_copy[0] = 100  # This won't affect the original
shallow_copy[2][0] = 300  # This will affect the original's nested list

print("Original:", original)  
print("Shallow Copy:", shallow_copy) 

```

#### Views:
* A view provides a reference to the original object without creating a new object.
* Changes made through the view directly affect the original object because the view is simply another way of accessing the original data.
* We will see in the next classes that NumPy arrays and Pandas DataFrames often deal with views when you slice or manipulate them.
* This a test 

```python
import numpy as np
arr = np.array([1, 2, 3, 4])
view = arr[1:3]  # This creates a view, not a copy

view[0] = 100  # Modifies the original array

print("Original array:", arr)  
print("View:", view)  

```

# Functions

```python
def square(x):
    """Square of x."""
    return x*x

def cube(x):
    """Cube of x."""
    return x*x*x

# create a dictionary of functions
funcs = {
    'square': square,
    'cube': cube,
}

x = 3
print(square(x))
print(cube(x))

for func in sorted(funcs):
    print (func, funcs[func](x))
```

## Functions arguments


In Python, whether arguments passed to a function are treated as views or copies depends on the data type of the argument and how it is handled inside the function. Here's how Python handles various types of arguments:

**Immutable Types** (e.g., integers, strings, tuples):
* For immutable types like `int`, `str`, and `tuple`, when you pass them as arguments to a function, Python creates a copy of the reference to the object, not the object itself.
* Since these objects cannot be modified, any attempt to change them inside the function results in the creation of a new object, leaving the original object unchanged.

```python
def modify(x):
    x += 1
    print("Inside function:", x)

a = 10
modify(a)
print("Outside function:", a)

```

**Mutable Types** (e.g., lists, dictionaries, sets):
* For mutable types like `list`, `dict`, or `set`, Python passes a reference to the original object. This means that any modification made to the object inside the function will affect the original object outside the function, as they both reference the same object (this behaves like a view).

```python
def modify_list(lst):
    lst.append(4)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

```

## Higher order functions

A function that uses another function as an input argument or returns a function is known as a higher-order function (HOF). The most familiar examples are `map` and `filter`.


### map

The map function applies a function to each member of a collection

```python
x = list(map(square, range(5))) 
print (x)

# Note the difference w.r.t python 2. In python 3 map retuns an iterator so you can do stuff like:
for i in map(square,range(5)): print(i)

# or
[i for i in map(square,range(6))]
```

### filter

The filter function applies a predicate to each member of a collection, retaining only those members where the predicate is True

```python
def is_even(x):
    return x%2 == 0

print (list(filter(is_even, range(5))))
```

Combinations in sequence of HOF are obviously possible

```python
list(map(square, filter(is_even, range(5))))
```

### reduce

The reduce function reduces a collection using a binary operator to combine items two at a time. More often than not reduce can be substituted with a more efficient for loop. It is worth mentioning it for its key role in big-data applications together with map (the map-reduce paradigm). 
N.B.: it no loger exist as built-in function in python 3, it is now part of the `functools` library

```python
from functools import reduce

def my_add(x, y):
    return x + y

# another implementation of the sum function
reduce(my_add, [1,2,3,4,5])
```

### zip

zip is useful when you need to iterate over matched elements of multiple lists

```python
xs = [1, 2, 3, 4]
ys = [10, 20, 30, 40]
zs = ['a', 'b', 'c',]

for x, y, z in zip(xs, ys, zs):
    print (x, y, z)
```

### Custom HOF

```python
def custom_sum(xs, transform):
    """Returns the sum of xs after a user specified transform."""
    return sum(map(transform, xs))

xs = range(5)
print (custom_sum(xs, square))
print (custom_sum(xs, cube))


```

### Returning a function

```python
def make_logger(target):
    def logger(data):
        with open(target, 'a') as f:
            f.write(data + '\n')
    return logger

foo_logger = make_logger('foo.txt') #foo.txt will be created if not there already
foo_logger('Hello')
foo_logger('World')
```

```python
! cat 'foo.txt'
```

<!-- #region -->
## Anonimous functions (lambda)

When using functional style, there is often the need to create specific functions that perform a limited task as input to a HOF such as map or filter. In such cases, these functions are often written as anonymous or lambda functions. 
The syntax is as follows:

lambda *arguments* : *expression*


If you find it hard to understand what a lambda function is doing, it should probably be rewritten as a regular function.
<!-- #endregion -->

```python
suml = lambda x,y: x+y
suml(3,4)
```

```python
(lambda x,y: x+y)(3,4)
```

```python
for i in map(lambda x: x*x, range(5)): print (i)
```

```python
# what does this function do?
from functools import reduce
s1 = reduce(lambda x, y: x+y, map(lambda x: x**2, range(1,10)))
print(s1)

```

## Recursive functions 

```python
def fib1(n):
    """Fib with recursion."""

    # base case
    if n==0 or n==1:
        return 1
    # recursive case
    else:
        return fib1(n-1) + fib1(n-2)

    
print ([fib1(i) for i in range(10)])
```

```python
# In Python, a more efficient version that does not use recursion is

def fib2(n):
    """Fib without recursion."""
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b

print ([fib2(i) for i in range(10)])
```

```python
# check indeed the timing:

%timeit fib1(20)
%timeit fib2(20)

```

## Iterators

Iterators represent streams of values. Because only one value is consumed at a time, they use very little memory. Use of iterators is very helpful for working with data sets too large to fit into RAM.

```python
# Iterators can be created from sequences with the built-in function iter()

xs = [1,2,3]
x_iter = iter(xs)

print (next(x_iter))
print (next(x_iter))
print (next(x_iter))
print (next(x_iter))
```

```python
# Most commonly, iterators are used (automatically) within a for loop
# which terminates when it encouters a StopIteration exception

x_iter = iter(xs)
for x in x_iter:
    print (x)
```

## More on comprehensions

```python
# A generator expression

print ((x for x in range(10)))

# A list comprehesnnion

print ([x**2 for x in range(10)])

# A set comprehension

print ({x for x in range(10)})

# A dictionary comprehension

print ({str(x): x**2 for x in range(10) if x%2==0})
```

## Useful Modules

You may want to have a look at the content of the following modules for further usage of (HO) functions:
  - [operator](https://docs.python.org/3/library/operator.html)
  - [functools](https://docs.python.org/3/library/functools.html)
  - [itertools](https://docs.python.org/3/library/itertools.html)
  - [toolz](https://pypi.org/project/toolz/)
  - [funcy](https://pypi.org/project/funcy/)


## Decorators

Decorators are a type of HOF that take a function and return a wrapped function that provides additional useful properties.

Examples:

  - logging
  - profiling
  - Just-In-Time (JIT) compilation

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
```

```python
say_whee()
```

Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

```python
say_whee()
```

#### JIT

A JIT (Just-In-Time) compiler refers to a technique used to improve the performance of code execution by compiling code into machine code at runtime, rather than interpreting it line by line. This helps speed up program execution by reducing the overhead of repeatedly interpreting code.

While the standard Python interpreter, CPython, does not include a JIT compiler, there are alternative Python implementations that provide JIT compilation, such as PyPy or [numba](https://numba.pydata.org).

JIT combines both interpretation and compilation. It interprets code initially, and as it identifies sections of code that are executed repeatedly, it compiles them to machine code, optimizing performance dynamically.



```python
from numba import jit

@jit(nopython=True)
def fast_sum(arr):
    total = 0.0  # check thi 
    for i in arr:
        total += i
    return total

```

```python
#fast_sum(list(range(100)))
#fast_sum([1,2,3,4,5])

arr = np.arange(int(1e6), dtype=np.float64)
print(fast_sum(arr))

# is it really fast? Try to compare with my_add above
```

# Classes and Objects

Old school object-oriented programming is possible and often used in python. Classes are defined similarly to standard object-oriented languages, with similar functionalities.

The main python doc [page](https://docs.python.org/3/tutorial/classes.html) is worth reading through 

```python
class Pet:
    # the "constructor"
    def __init__(self, name, age):  #inizialize the elements of the class
        self.name=name
        self.age=age
    # class functions take the "self" parameter !!!
    def set_name(self,name):
        self.name=name
    def convert_age(self,factor):
        self.age*=factor

buddy=Pet("buddy",4)
print (buddy.name, buddy.age)
buddy.age=3
print (buddy.convert_age(4))
print (buddy.age)

```

```python
# ineritance is straightforward
class Dog(Pet):
    # the following variables is "global", i.e. holds for all "Dog" objects
    species = "mammal"
    # functions can be redefined as usual
    def convert_age(self):
        self.age*=7
    def set_species(self, species):
        self.species = species
        
puppy=Dog("tobia",10)
print(puppy.name)
puppy.convert_age()
print(puppy.age)


```

```python
from numba import jit
import numpy as np

@jit(nopython=True)
def fast_sum(arr):
    total = 0.0  # float to match arr.dtype
    for i in arr:
        total += i
    return total

arr = np.arange(1_000_000, dtype=np.float64)
print(fast_sum(arr))

```

```python

```
