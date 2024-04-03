# [LeetCode 567 - Permutation in String](https://leetcode.com/problems/permutation-in-string)


## Description

<p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code><em> if </em><code>s2</code><em> contains a permutation of </em><code>s1</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>&#39;s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidbaooo&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidboaoo&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>

<br/>

## Solution 1

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n])
        if cnt1 == cnt2:
            return True
        for i in range(n, len(s2)):
            cnt2[s2[i]] += 1
            cnt2[s2[i - n]] -= 1
            if cnt1 == cnt2:
                return True
        return False
```

#### JAVA:
```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length();
        int m = s2.length();
        if (n > m) {
            return false;
        }
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for (int i = 0; i < n; ++i) {
            ++cnt1[s1.charAt(i) - 'a'];
            ++cnt2[s2.charAt(i) - 'a'];
        }
        if (Arrays.equals(cnt1, cnt2)) {
            return true;
        }
        for (int i = n; i < m; ++i) {
            ++cnt2[s2.charAt(i) - 'a'];
            --cnt2[s2.charAt(i - n) - 'a'];
            if (Arrays.equals(cnt1, cnt2)) {
                return true;
            }
        }
        return false;
    }
}
```
#### C++:
```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        if (n > m) {
            return false;
        }
        vector<int> cnt1(26), cnt2(26);
        for (int i = 0; i < n; ++i) {
            ++cnt1[s1[i] - 'a'];
            ++cnt2[s2[i] - 'a'];
        }
        if (cnt1 == cnt2) {
            return true;
        }
        for (int i = n; i < m; ++i) {
            ++cnt2[s2[i] - 'a'];
            --cnt2[s2[i - n] - 'a'];
            if (cnt1 == cnt2) {
                return true;
            }
        }
        return false;
    }
};
```

<!-- tabs:end -->

<br/>

## Solution 2

<!-- tabs:start -->

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        cnt = Counter()
        for a, b in zip(s1, s2):
            cnt[a] -= 1
            cnt[b] += 1
        diff = sum(x != 0 for x in cnt.values())
        if diff == 0:
            return True
        for i in range(n, m):
            a, b = s2[i - n], s2[i]

            if cnt[b] == 0:
                diff += 1
            cnt[b] += 1
            if cnt[b] == 0:
                diff -= 1

            if cnt[a] == 0:
                diff += 1
            cnt[a] -= 1
            if cnt[a] == 0:
                diff -= 1

            if diff == 0:
                return True
        return False
```

<!-- tabs:end -->

<!-- end -->
