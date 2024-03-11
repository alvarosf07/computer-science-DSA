# Problem #02 - Find Max Number in List

## Python

### Solution 1 - Use `for` Loop

```python
def find_max(list):
    max = None    
    for i in list:
        if i > max:
            max = i
    return max
```

### Solution 2 - Use Function `max()`
```python
max(list)
```

### Solution 3 - Use List Comprehension
Not very efficient space-wise, since we need to create a whole new list
```python
list=[1,2,3,4,5,6]
max=0

print ([e for e in list if e>max][-1])
```

### Solution 4 - Sort List
```python
list=[1,2,3,4,5,6]

print (sorted(list)[-1])                #[1,2,3,4,5,6][-1]
print (sorted(list, reverse=True)[0])   #[6,5,4,3,2,1][0]
```
