# Overview
1. [Pythonic](#pythonesk)
2. [Automated tests](#automated-tests)
3. [List comprehensions](#list-comprehensions)
4. [Iterables and generators](#iterables-and-generators)
10. [Other](#other)


# Pythonic
A style guide for python code can be found [here](https://peps.python.org/pep-0008/).
Or you can just run this in python:
```python
import this
```
> The Zen of Python, by Tim Peters  
Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!

Key takeaways are:
- Indent with 4 spaces, not with tabs
- Name variables so they don't need further explanation
- Annotate variable types
- Functions should only do one task
- Classes should be used if necessary
- Exception handling should be narrowed down to each specific error type
- Produce code that is clear, concise and maintainable
- Write automated tests to always ensure functionality

## Type annotation
Type annotations are a form of documentation and make code more readable.
In built types can be annotated without any extra steps.
However, to specify the type of the elements in an iterable it requires
```python
from typing import List, Dict, Optional, Callable
values: List[int] = []
counts: Dict[str, int] = {"libaries": 1, "imports": 4}
optional_arg: Optional[float] = None

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s,2)

def comma_repeater(s: str, n: int) -> str:
    return ", ".join([s for _ in range(n)])

assert twice(comma_repeater, "type annotation") == "type annotation, type annotation"
```


## Automated tests
Python offers the assert functionality for testing conditions, which will throw in Assertion Error if the condition is false.
An optional message can be added to the line that will be printed with the Assertion Error message.
```python
assert name == "John Doe", f"The name was '{name}' instead"
```

# List comprehensions
List comprehensions are an elegant and easy way to create lists on the basis of possibly multiple for-loops and conditions.
Each loop can access the iterating variables of any preceding loop. Conditions in list comprehensions are written in ternary if-then-else statements, though else statements are not possible in list comprehensions. 
```python
even_pairs = [(x,y) for x in range(10000) if x%2==0 for y in range(10000) if y%2==0]
```
Less common, but still possible, are dictionary and set comprehensions.

# Iterables and generators
Iterables is any type over which one can iterate e.g. in a for-loop.
However, creating a list, like the one given in the [List comprehensions](#list-comprehensions) section, can take up a lot of memory.
Generators, on the other hand, are iterables which only yield a value just before it is used, hence, using less memory. A generator that is never used, will never produce any values.
```python
generator_even_pairs = ((x,y) for x in range(10000) if x%2==0 for y in range(10000) if y%2==0)

def generator_odd_pairs(n):
    x,y = 1,1
    while x < n:
        while y < n:
            yield x,y
            y += 2
        x += 2
```
This code will execute immediately because none of the generators will actually produce something, as they were never used.
But more importantly, the second generator is about 4.000 times more time-efficient than a list, when it comes to generating 25 million tuples.

```python
from time import perf_counter

# List comprehension
tic = perf_counter()
for x,y in [(x,y) for x in range(0, 10000, 2) for y in range(0, 10000, 2)]:
    sum_of_both = x+y
toc = perf_counter()
print(toc-tic) # Around 5 seconds

# Generator with comprehension
tic = perf_counter()
for x,y in ((x,y) for x in range(0, 10000, 2) for y in range(0, 10000, 2)):
    sum_of_both = x+y
toc = perf_counter()
print(toc-tic) # Less than 4 seconds

# Generator with yield
tic = perf_counter()
def generator_odd_pairs(n):
    x,y = 1,1
    while x < n:
        while y < n:
            yield x,y
            y += 2
        x += 2

for x,y in generator_odd_pairs(10000):
    sum_of_both = x+y
toc = perf_counter()
print(toc-tic) # Consistently less than 0.00125 seconds
```

# args and kwargs, zip and unpacking
Writing a function on a higher level of abstraction, which takes another function f as one of its arguments and returns a new arguments as a result, calls for the use of *args and **kwargs in case that the function f requires an unforeseen amount of arguments.
```python
def doubler(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

def f1():
    return 10
def f2(a, b):
    return a + b
def f3(a,b,c=1):
    return a*b*c
g1 = doubler(f1)
g2 = doubler(f2)
g3 = doubler(f3)

assert g1() == 20 # 10 * 2
assert g2(3,5) == 16 # (3 + 5) * 2
assert g3(1,2,3) == 12 # (1 * 2 * 3) * 2
```
The function created by the abstract function, passes down all arguments (args) and keyword-arguments (kwargs) given to the initial function and unpacks them with the * and ** operand, respectively.

Just like iterables can be zipped together with the zip-function, an iterable can be unpacked into its elements with the * operand. In order to reverse a zip, one has to write the following.

```python
nums = (1, 2, 3)
squares = (1, 4, 9)

square_tuples = [pair for pair in zip(nums, squares)]
nums2, squares2 = zip(*square_tuples)

assert nums2 == nums
assert squares2 == squares
```
Note that this unzipping method returned tuples

# Regular expressions
Regular expressions help to look for patterns in a word or text. There are many methods but some of them are:
```python
import re as regex # I don't like the abbreviation "re", as it can be easily overlooked or overwritten

assert not regex.match("a", "cat") # Match starts looking at the beginning
assert regex.search("a", "cat") # Search searches anywhere in the string
assert not regex.search("c", "dog")

# Anything in brackets is a set of characters, any single character in a set becomes a search criteria
assert len(regex.split("[ab]", "carbs")) == 3 # Splits at every occasion
assert regex.sub("[el]", "o", "Hello") == "Hoooo" # Substitutes at every occasion
```



# Other