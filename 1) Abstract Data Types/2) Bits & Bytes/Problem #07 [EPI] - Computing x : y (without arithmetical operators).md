# Elements of Programming Interviews 4.6 - Computing x/y without arithmetical operators


## Description

<p>Given two positive integers <code>a</code> and <code>b</code>, compute their quotient, using only the addition, subtraction and shifting operators.</p>

<p>&nbsp;</p>
<p><strong>Hint:</strong></p>

<ul>
	<li> Relate <code>x/y</code> to <code>(x-y)/y</code> </li>
</ul>

<br/>

## Solution

<p> A brute-force approach is to iteratively subtract y from r until what remains is less than y. The number of such subtractions is exactly the quotient, x/y, and the remainder is the term that's less than y. The complexity of the brute-force approach is very high, e.g. when $y = 1$ and $x = 2^{31}-1$, it will take $2^{31} - 1$ iterations. </p>

<p> A better approach is to try and get more work done in each iteration. For example, we can compute the largest k such that $2^k y \leq x$, subtract $2^k$ y from x, and add $2^k$ to the quotient. For example, if $x=(1011)$ and $y=(10)$, then $k=2$, since $2x2^2 \leq 11$ and $2x2^3 > 11$. We subtract (1000) from (1011) to get (11), add $2^k = 2^2 = (100)$ to the quotient, and continue by updating x to (11). </p>

<p> The advantage of using $2^ky$ is that it can be computed very efficiently using shifting, and r is at least halved in each iteration. If it takes <code>n</code> bits to represent x/y, there are O(n) iterations. If the largest k such that $2^ky \leq x$ is computed by iterating through k, each iteration has time complexity O(n). This leads to an O(n^2) algorithm. </p>

<p> A better way to find the largest k in each iteration is to recognize that it keeps decreasing. Therefore, instead of testing in each iteration whether $2^y,2^1y,2^2y$,. . . is less than or equal to r, after we initially find the largest k such that $2^k y \leq x $, subsequent iterations we test $2^{k-1}y, 2^{k-2}y, 2^{k-3} y $, . . . with x. </p>

In essence, the program applies the grade-school division algorithm to binary numbers. With each iteration, we process an additional bit. Therefore, assuming individual shift and add operations take <code>O(1)</code> time, the time complexity is <code>O(n)</code>.

<!-- tabs:start -->

#### Python:
```python
class Solution:
    def divide (x , y) :
	result, power = 0, 32
	y_power = y << power
 	while x >= y:
		while y_power > x:
			y_power >>= 1
			power -= 1
		result += 1 << power
		x -= y_power
	return result
```

<!-- tabs:end -->

<!-- end -->
