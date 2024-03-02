# Elements of Programming Interviews 4.6 - Computing x/y without arithmetical operators


## Description

<p>Given two positive integers <code>a</code> and <code>b</code>, compute their quotient, using only the addition, subtraction and shifting operators.</p>

<p>&nbsp;</p>
<p><strong>Hint:</strong></p>

<ul>
	<li> Relate <code>x/y</code> to <code>(x-y)/y</code> </li>
</ul>

<br/>

## Solutions

### Solution 1
<p> A brute-force approach is to iteratively subtract y from r until what remains is less than y. The number of such subtractions is exactly the quotient, xf y, and the remainder is the term that's less than y. The complexity of the brute-force approach is very high, e.g. when y = L and r = 231 -1, it will take 231 - 1 iterations. </p>
<p> A better approach is to try and get more work done in each iteration. For example, we can compute the largest k such that 2!'y < x, subtract 2l'y from x, and add 2ft to the quotient. For example,i6s=(1011)zandA=(l})z,thenk=2,since2x22< 11 and2x23> 11. We subtract (1000)2 from (1011)2 to get (11)2, add 2k = 22 = (100)2 to the quotient, and continue by updating r to (11)_2. </p>
<p> The advantage of using 2ky is that it can be computed very efficiently using shifting, and r is at least halved in each iteration. If it takes rz bits to represent x/y, there are O(n) iterations. If the largest k such that <code> 2ky < r </code> is computed by iterating through k, each iteration has time complexity O(n). This leads to an O(n^2) algorithm. </p>
<p> A better way to find the largest k in each iteration is to recognize that it keeps decreasing. Therefore, instead of testing in each iteration whether $2^y,2^1y,2^2y$,. . . is less than or equal to r, after we initially find the largest k such that $2^k y \leq x $, subsequent iterations we test $2^{k-1}y, 2^{k-2}y, 2^{k-3} y $, . . . with x. </p>

The number of multiplications is at most twice the index of y's MSB, implying an O(n) time complexity.

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def power (x , y) :
	result, power = 1.0, y
	if y < 0:
		power, x = -power, 1.0/x
	while power:
		if power & 1:
			result *= x
		x, power = x * x, power >> 1
	return result
```

<!-- tabs:end -->

<!-- end -->
