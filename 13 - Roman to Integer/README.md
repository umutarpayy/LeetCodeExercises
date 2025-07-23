# 13. Roman to Integer

**Difficulty:** Easy  
**Status:** Solved

## Problem Description

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Examples

### Example 1:
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

### Example 2:
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

### Example 3:
```
Input: s = "MCMXC"
Output: 1990
Explanation: M = 1000, CM = 900, XC = 90.
```

## Constraints

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## My Solution

```python
class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        
        for char in s:
            current_value = roman_to_int[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        
        return total
```

### Explanation

This solution uses a **single-pass approach with subtraction detection**:

1. **Dictionary mapping**: Create a mapping from Roman symbols to their integer values
2. **Initialize variables**: Set `total = 0` and `prev_value = 0` for tracking
3. **Iterate through string**: For each character, get its numeric value
4. **Subtraction logic**: 
   - If `current_value > prev_value`: We found a subtraction case (like IV, IX, etc.)
   - Subtract `2 * prev_value` because we already added `prev_value` in the previous iteration
   - Add `current_value` to get the correct result
5. **Normal addition**: If no subtraction case, simply add the current value
6. **Update previous**: Set `prev_value = current_value` for next iteration

### Algorithm Walkthrough

**Example: "IV" = 4**
- **I**: current=1, prev=0 → 1≯0 → total = 0+1 = 1, prev=1  
- **V**: current=5, prev=1 → 5>1 ✓ → total = 1+5-2×1 = 4, prev=5

**Example: "MCMXC" = 1990**
- **M**: current=1000, prev=0 → total = 1000, prev=1000
- **C**: current=100, prev=1000 → total = 1100, prev=100  
- **M**: current=1000, prev=100 → 1000>100 ✓ → total = 1100+1000-200 = 1900, prev=1000
- **X**: current=10, prev=1000 → total = 1910, prev=10
- **C**: current=100, prev=10 → 100>10 ✓ → total = 1910+100-20 = 1990, prev=100

**Time Complexity**: O(n) - single pass through the string  
**Space Complexity**: O(1) - constant extra space for the dictionary

**Key Insight**: The `-2 * prev_value` handles the subtraction rule elegantly by "undoing" the previous addition and applying the correct subtraction. 