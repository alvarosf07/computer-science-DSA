# [LeetCode 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)


## Description

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

<br/>

## Solutions

### Solution 1 - Brute Force
List all substrings from highest length to lowest, and return the first substring without repeating characters.
<!-- tabs:start -->
```python
def lengthLongestNonRepSubstring(s: str) -> int:
    for l in range (len(s),0,-1):
	for i in range(len(s)+1-l):  
	    if l==len(set(s[i:i+l])):
		return l
    return 0
```
<!-- tabs:end -->

<br/>

### Solution 2
Solution with good memory complexity but bad time complexity:

<!-- tabs:start -->
```python
def lengthLongestNonRepSubstring(s: str) -> int:
    for l in range (len(s),0,-1):
	for i in range(len(s)+1-l):  
	    if l==len(set(s[i:i+l])):
		return l
    return 0
```
<!-- tabs:end -->


<br/>

### Solution 3 - Two pointers + Hash Table

Define a hash table to record the characters in the current window. Let $i$ and $j$ represent the start and end positions of the non-repeating substring, respectively. The length of the longest non-repeating substring is recorded by `ans`.

For each character $s[j]$ in the string `s`, we call it $c$. If $c$ exists in the window $s[i..j-1]$, we move $i$ to the right until $s[i..j-1]$ does not contain `c`. Then we add `c` to the hash table. At this time, the window $s[i..j]$ does not contain repeated elements, and we update the maximum value of `ans`.

Finally, return `ans`.

The time complexity is $O(n)$, where $n$ represents the length of the string `s`.

Two pointers algorithm template:

```java
for (int i = 0, j = 0; i < n; ++i) {
    while (j < i && check(j, i)) {
        ++j;
    }
    // logic of specific problem
}
```

<!-- tabs:start -->

#### Python:
```python
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
	ss = set()
	i = ans = 0
	for j, c in enumerate(s):
	    while c in ss:
		ss.remove(s[i])
		i += 1
	    ss.add(c)
	    ans = max(ans, j - i + 1)
	return ans
```

#### Java:
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> ss = new HashSet<>();
        int i = 0, ans = 0;
        for (int j = 0; j < s.length(); ++j) {
            char c = s.charAt(j);
            while (ss.contains(c)) {
                ss.remove(s.charAt(i++));
            }
            ss.add(c);
            ans = Math.max(ans, j - i + 1);
        }
        return ans;
    }
}
```
#### C++:
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> ss;
        int i = 0, ans = 0;
        for (int j = 0; j < s.size(); ++j) {
            while (ss.count(s[j])) ss.erase(s[i++]);
            ss.insert(s[j]);
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
```

<!-- tabs:end -->


<br/>

### Solution 4 - Two-Pointers Solution (Moving Dictionary)

<!-- tabs:start -->

```python
def lengthLongestNonRepSubstring2(s: str) -> int:
	cs = {}
	b = 0
	maxl = 0

	if s=="": return 0
	for i in range (len(s)):
	    if s[i] not in cs:
		cs[s[i]]=i
		if len(cs)>maxl: maxl=len(cs)
	    else:
		if len(cs)>maxl: maxl=len(cs)
		b = cs[s[i]]+1
		cs = {key:val for key, val in cs.items() if val>=b}
		cs[s[i]]=i

	return maxl
```

<!-- tabs:end -->


<br/>

### Solution 5 - Two pointers solution (dictionary + moving pointers only)

<!-- tabs:start -->

```python
def lengthLongestNonRepSubstring2(s: str) -> int:
	cs = {}
	b = 0
	maxl = 0

	if s=="": return 0
	for i in range (len(s)):
	    if s[i] not in cs:
		cs[s[i]]=i
		if len(cs)>maxl: maxl=len(cs)
	    else:
		if len(cs)>maxl: maxl=len(cs)
		b = cs[s[i]]+1
		cs = {key:val for key, val in cs.items() if val>=b}
		cs[s[i]]=i

	return maxl
```

<!-- tabs:end -->



<!-- end -->
