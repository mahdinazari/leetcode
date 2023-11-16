from typing import List


class Solution:
    """
        Write a function to find the longest common prefix string amongst an array of strings.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        first_assign = False
        for item in strs:
            if prefix == [] and not first_assign:
                prefix = list(item)
                first_assign = True
                continue
            
            if len(prefix) > len(item):
                del prefix[len(item):]
            
            for index, i in enumerate(item):
                if len(prefix) > index:
                    if i != prefix[index]:
                        del prefix[index:]
                        break
                            
        return ''.join(prefix)
    
        
if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs)) # "fl"
    
    strs = ["dog", "racecar", "car"]
    print(solution.longestCommonPrefix(strs)) # ""
    