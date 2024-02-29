# [LeetCode 271 - Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings)


## Description

<p>Design an algorithm to encode <b>a list of strings</b> to <b>a string</b>. The encoded string is then sent over the network and is decoded back to the original list of strings.</p>

<p>Machine 1 (sender) has the function:</p>

<pre>
string encode(vector&lt;string&gt; strs) {
  // ... your code
  return encoded_string;
}</pre>

Machine 2 (receiver) has the function:

<pre>
vector&lt;string&gt; decode(string s) {
  //... your code
  return strs;
}
</pre>

<p>So Machine 1 does:</p>

<pre>
string encoded_string = encode(strs);
</pre>

<p>and Machine 2 does:</p>

<pre>
vector&lt;string&gt; strs2 = decode(encoded_string);
</pre>

<p><code>strs2</code> in Machine 2 should be the same as <code>strs</code> in Machine 1.</p>

<p>Implement the <code>encode</code> and <code>decode</code> methods.</p>

<p>You are not allowed to&nbsp;solve the problem using any serialize methods (such as <code>eval</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dummy_input = [&quot;Hello&quot;,&quot;World&quot;]
<strong>Output:</strong> [&quot;Hello&quot;,&quot;World&quot;]
<strong>Explanation:</strong>
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---&gt; Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dummy_input = [&quot;&quot;]
<strong>Output:</strong> [&quot;&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> contains any possible characters out of <code>256</code> valid ASCII characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Could you write a generalized algorithm to work on any possible set of characters?</p>

<br/>

## Solutions

### Solution 1

<!-- tabs:start -->

### Python:
```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return chr(257).join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        return s.split(chr(257))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

<!-- tabs:end -->

### Solution 2

<!-- tabs:start -->

### Python:
```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        ans = []
        for s in strs:
            ans.append('{:4}'.format(len(s)) + s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans = []
        i, n = 0, len(s)
        while i < n:
            size = int(s[i : i + 4])
            i += 4
            ans.append(s[i : i + size])
            i += size
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

<!-- tabs:end -->

<!-- end -->
