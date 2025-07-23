# 9. Palindrome Number

**Difficulty:** Easy  
**Status:** Solved

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Examples

### Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Constraints

- -2³¹ ≤ x ≤ 2³¹ - 1

## Follow-up
Could you solve it without converting the integer to a string?

## My Solution

```python
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
```

### Explanation

This solution uses a **string conversion approach**:

1. **Convert to string**: Transform the integer `x` to its string representation using `str(x)`
2. **Reverse the string**: Use Python's slice notation `[::-1]` to reverse the string
3. **Compare**: Check if the original string equals the reversed string
4. **Return result**: Return `True` if they match (palindrome), `False` otherwise

**Time Complexity**: O(n) - where n is the number of digits in x  
**Space Complexity**: O(n) - for storing the string representation

**Advantages**: 
- Very concise and readable code
- Leverages Python's powerful string slicing capabilities
- Easy to understand and implement

**Note**: This approach converts the number to a string, which is simple but uses extra space. The follow-up question asks for a solution without string conversion, which would involve mathematical operations to reverse the number. 