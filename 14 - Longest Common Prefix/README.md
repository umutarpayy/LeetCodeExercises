# 14. Longest Common Prefix

**Difficulty:** Easy  
**Status:** Solved

## Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Examples

### Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
Explanation: The longest common prefix is "fl".
```

### Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

## My Solution

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        common_prefix = ""
        for index in range(len(min(strs, key=len))):
            all_equal = True
            for element in range(1, len(strs)):
                if (strs[0][index] != strs[element][index]):
                    all_equal = False
                    return common_prefix
            common_prefix += strs[0][index]
        return common_prefix
```

### Explanation

This solution uses a **character-by-character comparison approach**:

1. **Find shortest string**: Use `min(strs, key=len)` to determine the maximum possible prefix length
2. **Character comparison**: For each position from 0 to shortest string length:
   - Compare the character at current position across all strings
   - Use the first string as reference: `strs[0][index]`
   - Check if all other strings have the same character at this position
3. **Early termination**: If any character doesn't match, immediately return current prefix
4. **Build prefix**: If all characters match at current position, add to `common_prefix`
5. **Return result**: Return the accumulated common prefix

### Algorithm Walkthrough

**Example: ["flower","flow","flight"]**
- **Position 0**: f,f,f → all match → prefix = "f"
- **Position 1**: l,l,l → all match → prefix = "fl"  
- **Position 2**: o,o,i → mismatch at "flight" → return "fl"

**Example: ["dog","racecar","car"]**
- **Position 0**: d,r,c → mismatch immediately → return ""

**Time Complexity**: O(S) where S is the sum of all characters in all strings (worst case)  
**Space Complexity**: O(1) - only using constant extra space for variables

**Key Features**:
- **Early exit**: Stops as soon as a mismatch is found
- **Efficient bounds**: Only iterates up to the shortest string length
- **Simple logic**: Uses straightforward character comparison without complex string operations 