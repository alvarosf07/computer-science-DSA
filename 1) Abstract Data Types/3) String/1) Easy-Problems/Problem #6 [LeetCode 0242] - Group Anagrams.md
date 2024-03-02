# [LeetCode 242 - Valid Anagram](https://leetcode.com/problems/valid-anagram)          ${\textsf{\color{lightgreen} [Easy] }}$


## Description

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code><em>, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

<br/>

## Solutions

### Solution 1: Counting

We first determine whether the length of the two strings is equal. If they are not equal, the characters in the two strings must be different, so return `false`.

Otherwise, we use a hash table or an array of length $26$ to record the number of times each character appears in the string $s$, and then traverse the other string $t$. Each time we traverse a character, we subtract the number of times the corresponding character appears in the hash table by one. If the number of times after subtraction is less than $0$, the number of times the character appears in the two strings is different, return `false`. If after traversing the two strings, all the character counts in the hash table are $0$, it means that the characters in the two strings appear the same number of times, return `true`.

The time complexity is $O(n)$, the space complexity is $O(C)$, where $n$ is the length of the string; and $C$ is the size of the character set, which is $C=26$ in this problem.

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True
```

#### JAVA:
```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            ++cnt[s.charAt(i) - 'a'];
            --cnt[t.charAt(i) - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
```

#### C++:
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> cnt(26);
        for (int i = 0; i < s.size(); ++i) {
            ++cnt[s[i] - 'a'];
            --cnt[t[i] - 'a'];
        }
        return all_of(cnt.begin(), cnt.end(), [](int x) { return x == 0; });
    }
};
```

<!-- tabs:end -->

### Solution 2

<!-- tabs:start -->

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

<!-- tabs:end -->

<!-- end -->
