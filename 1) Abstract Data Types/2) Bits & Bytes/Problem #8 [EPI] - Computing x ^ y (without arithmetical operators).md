# Elements of Programming Interviews 4.7 - Computing x/y without arithmetical operators


## Description

<p>Write a program that takes a double <code>x</code> and an integer <code>y</code> and retums <code>x^y</code> ($x^y$). You can ignore overflow and underflow..</p>

<p>&nbsp;</p>
<p><strong>Hint:</strong></p>

<ul>
	<li> Exploit mathematical properties of exponentiation. </li>
</ul>

<br/>

## Solutions

### Solution 1
<p> First, assume y is nonnegative. The brute-force algorithm is to form $x^2 = x \cdot x$, then $x^3 = x^2 \cdot x$, and so on. This approach takes y - 1 multiplications, which is $O(2^n)$, where n is the number of bits needed to represent y. </p>

<p> The key to efficiency is to try and get more work done with each multiplication, thereby using fewer multiplications to accomplish the same result. For example, to compute $1.1^21$, instead of starting with 1.1 and multiplying by 1.1 20 times, we could multiply 1.1 by $1.1^2 = 1.21$ 10 times for a total of 11 multiplications (one to compute $1.1^2$, and 10 additional multiplications by $1.21$). We can do still better by computing $1.1^3$, $1.1^4$, etc. </p>
	
<p> When y is a power of 2, the approach that uses the fewest multiplications is iterated squaring, i.e., forming $x, x^2, (x^2)^2 = x^4, (x^4)^2 = x^8,....$. To develop an algorithm that works for general y, it is instructive to look at the binary representation of y, as well as properties of exponentiation, specifically $x^{y_0+y_1} = x^{y_0 \cdot y_1}$. </p>
	
<p> We begin with some small concrete instances, first assuming that y is nonnegative. For example, $x^{(1010)} = x^{(101)+(101)} = x^{(101)} \cdot x^{(101)}$. Similarly, $x^{(101)} = x^{(100)+(1)} = x^{(100)} \cdot x = x^{(10)} \cdot x^{(10)} \cdot x$. </p>
<p> Generalizing, if the least significant bit of y is 0, the result is $(x^{y/2})^2$; otherwise, it is $x \cdot (x^{y/2})^2$. This gives us a recursive algorithm for computing $x^y$ when y is nonnegative. </p> 
	
<p> The only change when y is negative is replacing x by 1/x and y by -y. In the implementation below we replace the recursion with a while loop to avoid the overhead of function calls. <p> 

<p> The number of multiplications is at most twice the index of y's MSB, implying an O(n) time complexity. <p>

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
