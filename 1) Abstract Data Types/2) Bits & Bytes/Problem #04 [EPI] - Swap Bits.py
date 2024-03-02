# Problem extracted from the book: "Elements of Programming Interviews"
# https://translucent504.github.io/programming-interviews/epi42/

# A 64-bit integer can be viewed as an array of 64bits, with the bit at index 0 corresponding to the least significant bit (LSB), 
# and the bit at index 63 corresponding to the most significant bit (MSB). 
# Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j. 
# Figure 4.1 illustrates bit swapping for an 8-bit integer.

def swap_bits(x, i, j):
    """Swap the ith bit of x with the jth bit of x"""
    if ((x >> i) & 1) ^ ((x >> j) & 1):  # checks if ith and jth bits of x are not same
        # x ^= 2**i  # inverts ith bit
        # x ^= 2**j  # inverts jth bit
        # Instead of computing 2**i we can do (1 << i) which is the same thing
        # and instead of doing 2 assignments we can prepare a bit mask
        # and then do a flip XOR with 1 assignment:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x
