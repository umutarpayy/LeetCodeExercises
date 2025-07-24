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

                
                
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
