# 1. Two Sum

**Difficulty:** Easy  
**Status:** Solved

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists.

## Follow-up
Can you come up with an algorithm that is less than O(n²) time complexity?

## My Solution

```python
class Solution(object):
    def twoSum(self,nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

### Explanation

This solution uses a **brute force approach**:

1. **Outer loop**: Iterate through each index `i` from 0 to `len(nums)-1`
2. **Inner loop**: For each `i`, iterate through index `j` from `i+1` to `len(nums)-1`
3. **Check all pairs**: For each combination, check if `nums[i] + nums[j]` equals the target
4. **Return result**: When a matching pair is found, immediately return the indices `[i, j]`

**Time Complexity**: O(n²) - nested loops check all possible pairs  
**Space Complexity**: O(1) - no extra space used

**Advantages**: 
- Simple and straightforward implementation
- Guaranteed to find the solution since it checks all possible pairs
- No additional data structures required

**Note**: This approach examines every possible combination of two numbers in the array, ensuring the correct solution is found for any valid input.


