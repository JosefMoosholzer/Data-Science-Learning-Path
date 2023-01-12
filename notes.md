# Overview
1. [Pythonesk](#pythonesk)
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

# Iterables and generators

# args and kwargs, zip and unpacking

# Regular expressions

# Other