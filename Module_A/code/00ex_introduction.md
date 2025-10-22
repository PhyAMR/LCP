---
format:
  html:
  code-fold: true 
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

1. The MickeyMouse problem

a) Write a program that prints the numbers from 1 to 100. But for multiples of 3 print `Mickey` instead of the corresponding number and for the multiples of 5 print `Mouse`. For numbers which are multiples of both three and five print `MickeyMouse`

```python
def MickeyMouse():
  for i in range(1,101):
    if i%3 == 0 and i%5==0:
      print("MickeyMouse")
    elif i%3==0:
      print("Mickey")
    elif i%5==0:
      print("Mouse")
    else:
      print(i)


MickeyMouse()
```

b) Put the result in a tuple and substitute `Mickey` with `Donald` and `Mouse` with `Duck`

```python

```

2\. The swap function

Write a function that swap the values of two input variables x and y (whatever the type). Try to do that also without a temporary variable


```python
def swap(x,y):
    print(f"The location of x={x} is {id(x)}")
    print(f"The location of y={y} is {id(y)}")
    x,y=y,x
    print(f"The location of x={x} is {id(x)}")
    print(f"The location of y={y} is {id(y)}")
swap("h",2)  

```


```python
x,y="h",2

def swap_g():
    global x
    global y
    print(f"The location of x={x} is {id(x)}")
    print(f"The location of y={y} is {id(y)}")
    x,y=y,x
    print(f"The location of x={x} is {id(x)}")
    print(f"The location of y={y} is {id(y)}")
swap_g()
```

3\. Computing the distance

Write a function that calculates and returns the euclidean distance between two points *u* and *v*, where *u* and *v* are both 2-tuples *(x,y)*. For example, if *u=(3,0)* and *v=(0,4)*, the function should return 5

```python
def eu_dist(u,v):
    return ((v[0]-u[0])**2+(v[1]-u[1])**2)**(1/2)
print(eu_dist((3,0),(0,4)))
```

4\. Counting letters

Write a program to calculate the number of times each character occurs in a given string *s*. Ignore differneces in capitalization

```python
s="Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Mickey instead of the number and for the multiples of five print Mouse. \
For numbers which are multiples of both three and five print MickeyMouse"

def counter(s):
    dic={}
    for i in s:
        dic[i] = 1
    for i in s:
        if i in dic.keys():
            x = dic[i]
            x+=1
            dic[i]=x
    return dic
print(counter(s))
```

5\. Isolating the unique

Write a function that determines and count the unique numbers in the list *l*

```python
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def s(l):
    print(f"The unique numbers are: \n {set(l)} \n Where there are {len(set(l))} unique numbers of which {len(l)-len(set(l))} where repeated")

s(l)
```

6\. Combination of functions

Write two functions - one that returns the square of a number, and one that returns the cube. Now write a third function that returns the number raised to the 6th power using the two previous functions.


```python
def sq(x):
    return x**2
def cub(x):
    return x**3
def sixth(x):
    return sq(cub(x))
print(sixth(2)==2**6)
```

7\. Cubes

Create a list of the cubes of x for x in *[0, 10]* using:

a) a for loop


```python
a = []
for x in range(0,11):
    a.append(x**3)
print(a)
```

b) a list comprehension


```python
b = [x**3 for x in range(0,11)]
print(b)
```


8\. Nested list comprehension

A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3,4,5). Find and put in a tuple all unique Pythagorean triples for the positive integers a, b and c less than 100.

```python
x = [(a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if a**2+b**2==(c**2)] 
print(x)  
```

9\. Normalization

Write a function that takes a tuple of numbers and returns it with the entries normalized to one

```python
def norm(u):
  if u[0]<u[1]:
    print(f"{u[0]/u[1]},{u[1]/u[1]}")
  else:
      print(f"{u[0]/u[0]},{u[1]/u[0]}")
norm((50,5))
```
