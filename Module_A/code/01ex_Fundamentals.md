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

0\. Implement a function (whatever you want) and save it to a file (e.g. `function.py`). Import that file and use that function in this notebook.



1\. Write the following as a list comprehension

```python
# 1
ans = []
for i in range(3):
    for j in range(4):
        ans.append((i, j))
print (ans)

print([ (i,j) for j in range(4) for i in range(3)]) 

# 2
ans = map(lambda x: x*x, filter(lambda x: x%2 == 0, range(5)))
print (list(ans))

print([ x**2 for x in range(5) if x%2==0]) 


```

2\. Convert the following function into a pure function with no global variables or side effects

```python
x = 5
def f(alist):
    for i in range(x):
         alist.append(i)
    return alist

alist = [1,2,3]
ans = f(alist)
print (ans)
print (alist) # alist has been changed!

def f2(alist,x=5):
  import copy
  new_list = copy.copy(alist) 
  for i in range(x):
    new_list.append(i)
  return new_list
ans2=f2(alist)
print(ans2)
print(alist)
```

<!-- #region -->
3\. Write a `decorator` hello that makes every wrapped function print “Hello!”, i.e. something like:

```python
def hello(func):
    
    def wrapper(*args, **kwargs):
        print("Buona Giornata")
        func(*args)
    return wrapper 



@hello
def square(x):
    return x*x

print(square(2))
```


<!-- #endregion -->

4\. Write the factorial function so that it a) does and b) does not use recursion.


```python
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)

def factorial2(n):
  x=1
  if n == 0:
    return x
  for i in range(n):
    x*=i
  return x

print(factorial2(0))
```

<!-- #region -->
5\. Use HOFs (zip in particular) to compute the weight of a circle, a disk and a sphere, assuming different radii and different densities:

```python
densities = {"Al":[0.5,1,2],"Fe":[3,4,5],"Pb": [15,20,30]}
radii = [1,2,3]
```

where the entries of the dictionary's values are the linear, superficial and volumetric densities of the materials respectively.

In particular define a list of three lambda functions using a comprehension that computes the circumference, the area and the volume for a given radius.


```python
import numpy as np 

sup = [lambda r: 2*np.pi*r, lambda r: np.pi*r**2, lambda r: 4/3*np.pi*r**3]

for e,dens in densities.items():
  for r,d in zip(radii,dens, a):
     mass=d*[s(r) for s in sup] 
     print(mass)
```
<!-- #endregion -->

<!-- #region -->
6\. Edit the class defintion to add an instance attribute of is_hungry = True to the Dog class. Then add a method called eat() which changes the value of is_hungry to False when called. Figure out the best way to feed each dog and then output “My dogs are hungry.” if all are hungry or “My dogs are not hungry.” if all are not hungry. The final output should look like this:

`I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course. 
My dogs are not hungry.
`

```python
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age, is_hungry = True):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    

    def eat(self, eaten):
        if eaten:
           self.is_hungry = False 
        else:
           self.is_hungry = True

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
```
<!-- #endregion -->

```python

```
