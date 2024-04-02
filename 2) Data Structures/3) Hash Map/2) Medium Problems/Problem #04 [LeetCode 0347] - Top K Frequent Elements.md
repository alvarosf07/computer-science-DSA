# [LeetCode 347 - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

## Description

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>

<br/>

## Solution 1

<!-- tabs:start -->
#### Python:
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return [v[0] for v in cnt.most_common(k)]
```

#### JAVA: 
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Long> frequency = Arrays.stream(nums).boxed().collect(
            Collectors.groupingBy(Function.identity(), Collectors.counting()));
        Queue<Map.Entry<Integer, Long>> queue = new PriorityQueue<>(Map.Entry.comparingByValue());
        for (var entry : frequency.entrySet()) {
            queue.offer(entry);
            if (queue.size() > k) {
                queue.poll();
            }
        }
        return queue.stream().mapToInt(Map.Entry::getKey).toArray();
    }
}
```

#### C++:
```cpp
using pii = pair<int, int>;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (int v : nums) ++cnt[v];
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        for (auto& [num, freq] : cnt) {
            pq.push({freq, num});
            if (pq.size() > k) {
                pq.pop();
            }
        }
        vector<int> ans(k);
        for (int i = 0; i < k; ++i) {
            ans[i] = pq.top().second;
            pq.pop();
        }
        return ans;
    }
};
```

<!-- tabs:end -->

### Solution 2

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        hp = []
        for num, freq in cnt.items():
            heappush(hp, (freq, num))
            if len(hp) > k:
                heappop(hp)
        return [v[1] for v in hp]
```

<!-- tabs:end -->

<!-- end -->
