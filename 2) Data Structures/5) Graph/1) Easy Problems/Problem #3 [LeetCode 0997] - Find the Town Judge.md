
# [LeetCode 997 - Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/description/)


## Description

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
  1. The town judge trusts nobody.
  2. Everybody (except for the town judge) trusts the town judge.
  3. There is exactly one person that satisfies properties 1 and 2.

You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`. 
If a trust relationship does not exist in `trust` array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise.


#### Example 1:

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

#### Example 2:

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

#### Example 3:

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

<br/>

#### Constraints:
* <code>1 <= n <= 2 * 1000</code>
* <code>0 <= trust.length <= 2 * 10<sup>4</sup></code>
* `trust[i].length == 2`
* All the pairs of `trust` are unique
* `ai != bi`
* `1 <= ai, bi <= n`

<br/>


<br/>

## Solution 1 - DFS
The criteria to being a judge is that:

1. The judge believes no one than himself
2. Whole town i.e Everybody believes judge

So at the end of the statement the constraints leads to pointing out that any person that is trusted 
by `n-1` persons and the same person believes no one, then the preson is said to be a judge.

Solution algorithm:
* Create an array `Trusted` of size `n+1` to represent the total number of peoples in a town and initialize it with `0`.
* After initialization, whenever a person trust someone else than himself, the `trusted` value of that person should be decreased since that person is not satisfying the two conditions that were mentioned in the question.
* Also if a certain `x` person is trusted by others from town, than this `x` person value should be increased and those who trusted that `x` person there values should be decreased.
* Finally, traverse through every person of town. While traversing, if a person is found with `n-1` trusts than this person should be the judge. Return the index of that person.

#### ➤ [Python](https://leetcode.com/problems/find-the-town-judge/solutions/1663344/c-java-python3-javascript-everything-you-need-to-know-from-start-to-end):
```python
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (N+1)
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
            
        for i in range(1, len(Trusted)):
            if Trusted[i] == N-1:
                return i
        return -1
```

<br/>
