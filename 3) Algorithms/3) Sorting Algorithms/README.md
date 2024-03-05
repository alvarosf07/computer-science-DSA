# Introduction to Sorting Algorithms

Sorting algorithms are fundamental tools in computer science and are used to arrange a collection of items in a specific order. The order could be numerical, alphabetical, or based on some other criteria. There are various sorting algorithms, each with its own advantages, disadvantages, and optimal use cases.



## Most Relevant Sorting Algorithms

Below there's an introduction to eight of the most relevant sorting algorithms, classified from worst to best time complexity. Further details about the algorithms, their implementations and additional exercises can be found in the sub-directories of this folder.

1. **Bubble Sort:**
   - Time Complexity: O(n^2)
   - Description: Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. It continues this process until the list is sorted.

2. **Selection Sort:**
   - Time Complexity: O(n^2)
   - Description: Selection sort divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly selects the smallest element from the unsorted sublist and swaps it with the first element of the unsorted sublist.

3. **Insertion Sort:**
   - Time Complexity: O(n^2)
   - Description: Insertion sort builds a sorted sublist one element at a time by repeatedly taking the next element from the unsorted part of the list and inserting it into its correct position in the sorted sublist.

4. **Merge Sort:**
   - Time Complexity: O(n log n)
   - Description: Merge sort is a divide-and-conquer algorithm that divides the input list into smaller sublists, recursively sorts each sublist, and then merges them back together in sorted order.

5. **Quick Sort:**
   - Time Complexity: O(n log n) (average case), O(n^2) (worst case)
   - Description: Quick sort is another divide-and-conquer algorithm that selects a pivot element, partitions the list into two sublists based on the pivot, recursively sorts each sublist, and then combines them.

6. **Heap Sort:**
   - Time Complexity: O(n log n)
   - Description: Heap sort builds a max heap from the input list, repeatedly extracts the maximum element from the heap, and then rebuilds the heap until the list is sorted.

7. **Counting Sort:**
   - Time Complexity: O(n + k)
   - Description: Counting sort assumes that the input consists of integers within a specific range. It counts the number of occurrences of each element and then uses this information to place each element in the correct position in the output list.

8. **Radix Sort:**
   - Time Complexity: O(nk)
   - Description: Radix sort sorts integers by processing individual digits of the numbers. It starts by sorting the least significant digit and then moves to the most significant digit, using a stable sorting algorithm such as counting sort or insertion sort at each step.

These are just a few examples of sorting algorithms, each with its own advantages, disadvantages, and optimal use cases. The choice of sorting algorithm depends on factors such as the size of the input, the nature of the data, and the desired time and space complexity.
