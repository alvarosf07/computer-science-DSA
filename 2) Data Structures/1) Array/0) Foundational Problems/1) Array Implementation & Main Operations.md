# 1. Array Implementation & Main Operations - Python
There are three main ways to define and operate with Ararys in Python:
  * With Python Lists
  * With the Array Module
  * With the Numpy Module

Starting with the simplest form, with Python lists:

### Array Implementation
```python
arr = [1, 2, 3, 4, 5]
```
### Array Operation I - Element Access
```python
print(arr[0])  # Output: 1
```

### Array Operation II - Element Modification
```python
arr[0] = 10
print(arr)  # Output: [10, 2, 3, 4, 5]
```

### Array Operation III - Element Insertion
```python
arr.insert(2, 20)  # Insert 20 at index 2
print(arr)  # Output: [10, 2, 20, 3, 4, 5]
```

### Array Operation IV - Element Deletion
```python
del arr[3]  # Delete element at index 3
print(arr)  # Output: [10, 2, 20, 4, 5]
```
<br/>


The code snippets shown above represent the simplest form of dealing with arrays in Python, which is through Python Lists. Alternatively, it's also possible to implement and operate with arrays in Python using two other tools:


<details>
  <summary>Array Implementations & Main Operations - Using Python Array Module</summary>
  
  ```python
  from array import array
  
  # Creating an array of integers
  arr = array('i', [1, 2, 3, 4, 5])
  
  # Accessing elements
  print(arr[0])  # Output: 1
  
  # Modifying elements
  arr[0] = 10
  print(arr)  # Output: array('i', [10, 2, 3, 4, 5])
  
  # Inserting elements
  arr.insert(2, 20)  # Insert 20 at index 2
  print(arr)  # Output: array('i', [10, 2, 20, 3, 4, 5])
  
  # Deleting elements
  arr.remove(3)  # Remove element 3
  print(arr)  # Output: array('i', [10, 2, 20, 4, 5])

  ```

</details>

<details>
  <summary>Array Implementations & Main Operations - Using Python Numpy Module</summary>
  
  ```python
  import numpy as np

  # Creating an array
  arr = np.array([1, 2, 3, 4, 5])
  
  # Accessing elements
  print(arr[0])  # Output: 1
  
  # Modifying elements
  arr[0] = 10
  print(arr)  # Output: [10, 2, 3, 4, 5]
  
  # Inserting elements
  arr = np.insert(arr, 2, 20)  # Insert 20 at index 2
  print(arr)  # Output: [10, 2, 20, 3, 4, 5]
  
  # Deleting elements
  arr = np.delete(arr, 3)  # Delete element at index 3
  print(arr)  # Output: [10, 2, 20, 4, 5]

  ```

</details>

<br/>
<br/>

# 2. Array Implementation & Main Operations - C++
### Array Implementation
```cpp
int arr[5] = {1, 2, 3, 4, 5};
```
### Array Operation I - Element Access
```cpp
int arr[5] = {1, 2, 3, 4, 5};
cout << arr[0] << endl;  // Output: 1
```

### Array Operation II - Element Modification
```cpp
int arr[5] = {1, 2, 3, 4, 5};
arr[0] = 10;
cout << arr[0] << endl;  // Output: 10
```

### Array Operation III - Element Insertion
```cpp
int arr[5] = {1, 2, 3, 4, 5};
int index = 2;
int value = 20;
for (int i = 4; i >= index; i--) {
    arr[i + 1] = arr[i];
}
arr[index] = value;
for (int i = 0; i < 6; i++) {
    cout << arr[i] << " ";
}
cout << endl;  // Output: 10 2 20 3 4 5
```

### Array Operation IV - Element Deletion
```cpp
int arr[5] = {1, 2, 3, 4, 5};
int index = 3;
for (int i = index; i < 5; i++) {
    arr[i] = arr[i + 1];
}
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
cout << endl;  // Output: 10 2 20 4 5
```

<br/>
<br/>

# 3. Array Implementation & Main Operations - JAVA
### Array Implementation
```java
public class Main {
    public static void main(String[] args) {
        // Declaring and initializing an array
        int[] arr = {1, 2, 3, 4, 5};
    }
}
```
### Array Operation I - Element Access
```java
public class Main {
    public static void main(String[] args) {
        // Declaring and initializing an array
        int[] arr = {1, 2, 3, 4, 5};

        // Accessing Elements
        System.out.println(arr[0]);  // Output: 1
    }
}
```

### Array Operation II - Element Modification
```java
public class Main {
    public static void main(String[] args) {
        // Declaring and initializing an array
        int[] arr = {1, 2, 3, 4, 5};

        // Modifying elements
        arr[0] = 10;
        System.out.println(arr[0]);  // Output: 10
    }
}
```

### Array Operation III - Element Insertion
```java
public class Main {
    public static void main(String[] args) {
        // Declaring and initializing an array
        int[] arr = {1, 2, 3, 4, 5};

        // Inserting elements
        int[] newArr = new int[arr.length + 1];
        int index = 2;
        int value = 20;
        for (int i = 0; i < index; i++) {
            newArr[i] = arr[i];
        }
        newArr[index] = value;
        for (int i = index; i < arr.length; i++) {
            newArr[i + 1] = arr[i];
        }
        arr = newArr;
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();  // Output: 1 2 20 3 4 5

    }
}
```

### Array Operation IV - Element Deletion
```java
public class Main {
    public static void main(String[] args) {
        // Declaring and initializing an array
        int[] arr = {1, 2, 3, 4, 5};

        // Deleting elements
        int[] newArr2 = new int[arr.length - 1];
        index = 3;
        for (int i = 0; i < index; i++) {
            newArr2[i] = arr[i];
        }
        for (int i = index; i < arr.length - 1; i++) {
            newArr2[i] = arr[i + 1];
        }
        arr = newArr2;
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();  // Output: 1 2 4 5
    }
}
```

<br/>













