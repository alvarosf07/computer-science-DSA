# Problem #01 - Different Ways to Sum All Numbers of Array

## Python

### Solution 1 - Function `sum()`
```python
list = ['1','2','3','4', '5', '6']

s=sum(list)
```

### Solution 2 - With for loop
```python
list = ['1','2','3','4', '5', '6']

s=0
for e in list:
    s = s+e
```

### Solution 3 - Sum() + Comprehension
Useful if we need to convert the numbers to `int` first:
```python
list = ['1','2','3','4', '5', '6']

sum(int(i) for i in list)
```
