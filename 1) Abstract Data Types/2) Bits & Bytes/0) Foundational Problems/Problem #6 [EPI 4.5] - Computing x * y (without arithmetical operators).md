# Elements of Programming Interviews 4.5 - Compute x * y without arithmetical operations          ${\textsf{\color{orange} [Medium] }}$


## Description

<p> Write a program that multiplies two nonnegative integers. The only operators you are allowed to use are: </p>

<ul>
	<li> assignment,
	<li> the bitwise operators: <code> > </code> ,  <code> < </code> , <code> | </code> , <code> & </code> , <code> ~ </code> , <code> ^ </code>  and </li>
	<li> equality checks and Boolean combinations thereof.
</ul>

<p> You may use loops and functions that you write yourself. These constraints imply, for example, that you cannot use increment or decrement, or test if r < y. </p>

<p>&nbsp;</p>
<p><strong>Hint:</strong></p>
<p> Add using bitwise operations; multiply using shift-and-add </p>


<br/>

## Solutions

### Solution 1
A brute-force approach would be to perform repeated addition, i.e., initialize the result to 0 and then add x to it y times. For example, to form 5 x 3, we would start with 0 and repeatedly add 5, i.e., form 0 + 5,5 + 5,10 + 5. The time complexity is very high –as much as O($2^n$), where n is the number of bits in the input, and it still leaves open the problem of adding numbers without the presence of an add instruction.

The algorithm taught in grade-school for decimal multiplication does not use repeated addition-it uses shift and add to achieve a much better time complexity. We can do the same with binary numbers –to multiply x and y we initialize the result to 0 and iterate through the bits of x, adding 2ky to the result if the kth bit of r is 1. 

The value <code> 2^k y </code> can be computed by left-shifting <code> y </code> by <code> k </code>. Since we cannot use add directly, we must implement it. We apply the grade-school algorithm for addition to the binary case, i.e., compute the sum bit-by-bit, and "rippling" the carry along.

The time complexity of addition is O(n), where rz is the number of bits needed to represent the operands. Since we do r additions to perform a single multiplication, the total time complexity is o(n2).

<!-- tabs:start -->

#### Python:
```python
    def multiply (x, y) :
	def add(a, b):
		running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
		while temp_a or temp_b:
			ak, bk = a & k, b & k
			carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
			running_sum |= ak ^ bk ^ carryin
			carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)

		return running_sum | carryin

	running_sum = 0

	while x: # Examines each bit of x.
		if x & 1:
			running_sum = add(running_sum, y)
		x, y = x >> 1, y << 1

	return running_sum
```

<!-- tabs:end -->

<!-- end -->
