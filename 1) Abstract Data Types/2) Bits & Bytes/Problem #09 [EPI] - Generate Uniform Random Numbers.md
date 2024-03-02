# Elements of Programming Interviews 4.10 - Generate Uniform Random Numbers


## Description

<p>This problem is motivated by the following scenario. Six friends have to select a designated driver using a single unbiased coin. The process should be fair to everyone. </p>

<p> How would you implement a random number generator that generates a random integer <code>i</code> between <code>a</code> and <code>b</code>, inclusive, given a random number generator that produces <code>0</code> or <code>1</code> with equal probability? All values in <code>[a,b]</code> should be equally likely. </p>

<p>&nbsp;</p>
<p><strong>Hint:</strong></p>

<ul>
	<li> How would you mimic a three-sided coin with a two-sided coin? </li>
</ul>

<br/>

## Solution

<p> To generate a random number corresponding to a dice roll, i.e., a number between 1 and 6, we begin by making three calls to the random number generator (since $2^2-1 < (6-1) <2^3-1$). If this yields one of $(000)$, $(001)$, $(010)$, $(011)$, $(100)$, $(101)$, we return 1 plus the corresponding value. Observe that all six values between 1 and 6, inclusive, are equally likely to be returned. If the three calls yields one of (110), (111), we make three more calls. 
    
<p> Note that the probability of having to try again is 218, which is less than half. Since successive calls are independent, the probability that we require many attempts diminishes very rapidly, e.g., the probability of not getting a result in 10 attempts is $(2/8)^10$ which is less than one in a million. </p>

<p> Assuming the O/1-valued random number generator takes <code>O(1)</code> time, the time complexity is <code>O(log(b - a + 1))</code>. </p>

<!-- tabs:start -->

#### Python:
```python
def uniform_random(lower-bound, upper-bound):
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i=0, 0
        while (1 << i) < number_of_outcomes:
            # zero-one_randonO is the provided randon nunber generator
            result - (result << 1) | zero_one_random()
            i += 1
        if result < number-of-outcomes:
            break
    return result + Iower_bound
```

<!-- tabs:end -->

<!-- end -->
