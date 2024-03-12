# Problem #03 - Find Second Max Number in Array

## Case A - If the max is repeated, max is still the same number
### - Solution A.1 - Loop + Hold 2 max elements
```python
def second_max(lst):
    if len(lst) < 2:
        return None  # There is no second maximum if the list has less than 2 elements

    max_num = float('-inf')  # Initialize maximum number as negative infinity
    second_max_num = float('-inf')  # Initialize second maximum number as negative infinity

    for num in lst:
        if num >= max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num:
            second_max_num = num

    # If there is no second maximum number found, return None
    if second_max_num == float('-inf'):
        return None

    return second_max_num

# Example usage:
my_list = [3, 8, 1, 6, 9, 3, 2]
print("Second maximum number:", second_max(my_list))  # Output: 8
```

### - Solution A.2 - Function that eliminates max
```python
def second_max(lst):
    # Find the maximum number in the list
    max_num = max(lst)

    # Remove the maximum number from the list
    lst.remove(max_num)

    # Find the maximum number in the updated list, which is the second maximum
    second_max_num = max(lst)

    return second_max_num

# Example usage:
my_list = [3, 8, 1, 6, 9, 3, 2]
print("Second maximum number:", second_max(my_list))  # Output: 8
```

### - Solution A.3 - Sort list and select 2 position [1]
Not very computationally efficient, as sorting the list has already complexity `O(n log n)`.
```python
def second_max(lst):
    if len(lst) < 2:
        return None  # There is no second maximum if the list has less than 2 elements

    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)

    return sorted_list[1]

# Example usage:
my_list = [3, 8, 1, 6, 9, 3, 2]
print("Second maximum number:", second_max(my_list))  # Output: 8
```
<br/>

## Case B - If the max is repeated, max is a different number

### - Solution B.1 - Loop + Hold 2 max different elements
```python
def second_max(lst):
    if len(lst) < 2:
        return None  # There is no second maximum if the list has less than 2 elements

    max_num = float('-inf')  # Initialize maximum number as negative infinity
    second_max_num = float('-inf')  # Initialize second maximum number as negative infinity

    for num in lst:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num

    # If there is no second maximum number found, return None
    if second_max_num == float('-inf'):
        return None

    return second_max_num

# Example usage:
my_list = [3, 8, 1, 6, 9, 3, 2]
print("Second maximum number:", second_max(my_list))  # Output: 8
```

### - Solution B.2 - Function that eliminates all occurrences of the max number
```python
# Function thar eliminates all occurrences of a number in a list
def remove_all(lst, value):
    # Iterate through the list in reverse order to avoid index shifting
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            # Remove the current element if it matches the value
            del lst[I]
    return lst

def second_max(last):
    # Find the maximum number in the list
    max_num = max(lst)

    # Remove the maximum number from the list
    lst=remove_all(lst,max_num)

    # Find the maximum number in the updated list, which is the second maximum
    second_max_num = max(lst)

    return second_max_num

# Example usage:
my_list = [3, 8, 1, 6, 9, 3, 2]
print("Second maximum number:", second_max(my_list))  # Output: 8
```
### - Solution B.3 - Sort list and select 2 position [1] if not equal to max [0]
Not very computationally efficient, as sorting the list has already complexity `O(n log n)`.
```python
def second_max(lst):
    if len(lst) < 2:
        return None  # There is no second maximum if the list has less than 2 elements

    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)

    # Iterate through the sorted list to find the second maximum number
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] != sorted_lst[i - 1]:
            return sorted_lst[i]

    # If all elements are the same, there is no second maximum
    return None

# Example usage:
my_list = [3, 8, 1, 6, 9, 3, 2]
print("Second maximum number:", second_max(my_list))  # Output: 8
```
