---
title: "Python Tips"
date: 2021-03-13T14:48:33-08:00
draft: true
toc: true
images:
tags:
  - untagged
---

## Overview



### Tip 1: be explicit when checking: None, [], 0

`not var` return `True` for various different cases.
```python
>>> var = None
>>> not var
True
>>> var = 0
>>> not var
True
>>> var = []
>>> not var
True
```

So when you are writing if else condition, instead of
```
if not var:
```
it's better to be explicit
```
if var != None:
if len(var) == 0:
if var != 0:
```

### Tip 1: sorted function with lambda key

`sorted` function
```python
sorted(iterable, key=None)
```

`lambda` function

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
```python
lambda arguments : expression
```
Examples:
```python
# Example 1: sort by attribute
sorted(students, key=lambda student: student.age)
# Example 2: sort by tuple(count, num), first sort with count, then sort with num
counter = Counter(arr)
sorted(arr, key=lambda num: (c[num], num) )
```
