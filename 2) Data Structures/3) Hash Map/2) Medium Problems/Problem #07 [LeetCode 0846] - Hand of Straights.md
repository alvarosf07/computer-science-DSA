# [LeetCode 846 - Hand of Straights](https://leetcode.com/problems/hand-of-straights)


## Description

<p>Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size <code>groupSize</code>, and consists of <code>groupSize</code> consecutive cards.</p>

<p>Given an integer array <code>hand</code> where <code>hand[i]</code> is the value written on the <code>i<sup>th</sup></code> card and an integer <code>groupSize</code>, return <code>true</code> if she can rearrange the cards, or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice&#39;s hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,4,5], groupSize = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice&#39;s hand can not be rearranged into groups of 4.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hand.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hand[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= groupSize &lt;= hand.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1296: <a href="https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a></p>

<br/>

## Solution 1

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        for v in sorted(hand):
            if cnt[v]:
                for x in range(v, v + groupSize):
                    if cnt[x] == 0:
                        return False
                    cnt[x] -= 1
                    if cnt[x] == 0:
                        cnt.pop(x)
        return True
```

#### JAVA:
```java
class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int v : hand) {
            cnt.put(v, cnt.getOrDefault(v, 0) + 1);
        }
        Arrays.sort(hand);
        for (int v : hand) {
            if (cnt.containsKey(v)) {
                for (int x = v; x < v + groupSize; ++x) {
                    if (!cnt.containsKey(x)) {
                        return false;
                    }
                    cnt.put(x, cnt.get(x) - 1);
                    if (cnt.get(x) == 0) {
                        cnt.remove(x);
                    }
                }
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
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        unordered_map<int, int> cnt;
        for (int& v : hand) ++cnt[v];
        sort(hand.begin(), hand.end());
        for (int& v : hand) {
            if (cnt.count(v)) {
                for (int x = v; x < v + groupSize; ++x) {
                    if (!cnt.count(x)) {
                        return false;
                    }
                    if (--cnt[x] == 0) {
                        cnt.erase(x);
                    }
                }
            }
        }
        return true;
    }
};
```

<!-- tabs:end -->
<br/>

## Solution 2

<!-- tabs:start -->

```python
from sortedcontainers import SortedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        sd = SortedDict()
        for h in hand:
            if h in sd:
                sd[h] += 1
            else:
                sd[h] = 1
        while sd:
            v = sd.peekitem(0)[0]
            for i in range(v, v + groupSize):
                if i not in sd:
                    return False
                if sd[i] == 1:
                    sd.pop(i)
                else:
                    sd[i] -= 1
        return True
```

<!-- tabs:end -->

<!-- end -->
