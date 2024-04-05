# [LeetCode 767 - Reorganize String](https://leetcode.com/problems/reorganize-string)


## Description

<p>Given a string <code>s</code>, rearrange the characters of <code>s</code> so that any two adjacent characters are not the same.</p>

<p>Return <em>any possible rearrangement of</em> <code>s</code> <em>or return</em> <code>&quot;&quot;</code> <em>if not possible</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> "aba"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaab"
<strong>Output:</strong> ""
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<br/>

## Solution 1 - Sorting Array
In this approach, we sort the array of characters by their frequency and then place them at alternate positions in the result string. This ensures that no two adjacent characters are the same.

#### Process:
1. Initialization:
	* Count the frequency of each character in the string.
	* Sort the array of characters based on their frequency in descending order.

2. Processing Each Character:
	* Start placing the most frequent characters first. Place them at even indices (0, 2, 4, ...).
	* Next, place the remaining characters at the odd indices (1, 3, 5, ...).
	* During this process, if the most frequent character appears more than (length of string+1)/2(\text{length of string} + 1) / 2(length of string+1)/2 times, return an empty string as reorganization is not possible.

3. Wrap-up:
	* Combine all the individual characters to form the final reorganized string.

#### Complexity: 
* Time Complexity: `O(n+klogk)`
	* `O(n)` for counting the frequency of each character in the string.
	* `O(klog⁡k)` for sorting the unique characters by their frequency.
	* `O(n)` for placing the characters into the new string. Here, you iterate through each character, inserting them into their respective places in the result string.

* Space Complexity: `O(n)`

<br/>

#### Python Code:
```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
            
        sorted_chars = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        
        if freq_map[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""
        
        res = [None] * len(s)
        
        i = 0
        for char in sorted_chars:
            for _ in range(freq_map[char]):
                if i >= len(s):
                    i = 1
                res[i] = char
                i += 2
                
        return "".join(res)
```
<br/>


## Solution 2 - Priority Queue (Heap)
The priority queue approach leverages a max heap to maintain the frequency of each character. By doing so, we can alternate the most frequent characters with the remaining ones to ensure no adjacent characters are the same.

#### Process:
1. Initialization:
	* Count the frequency of each character in the string.
	* Populate the max heap with these frequencies.

2. Processing Each Character:
	* Pop the top two characters from the max heap (i.e., the ones with the highest frequency).
	* Append these two characters to the result string.
	* Decrement their frequencies and re-insert them back into the max heap.
	* If only one character remains in the heap, make sure it doesn't exceed half of the string length, otherwise, return an empty string.

3. Wrap-up:
	* If there's a single remaining character with a frequency of 1, append it to the result.
	* Join all the characters to return the final reorganized string.

#### Complexity: 
* Time Complexity: `O(nlogk)`
	* `O(n)` for counting the frequency of each character in the string. Here, nnn is the length of the string.
	* `O(klogk)` for building the max heap, where kkk is the number of unique characters in the string.
	* The heap operations (insertion and deletion) would require `klogk` time each. In the worst-case scenario, you would be doing these operations nnn times (once for each character in the string).

* Space Complexity: `O(n)`

<br/>

#### Python Code:
```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
            
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)
        
        res = []
        
        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)
            
            res.extend([char1, char2])
            
            if freq1 + 1 < 0:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(max_heap, (freq2 + 1, char2))
                
        if max_heap:
            freq, char = heapq.heappop(max_heap)
            if -freq > 1:
                return ""
            res.append(char)
            
        return "".join(res)
```
