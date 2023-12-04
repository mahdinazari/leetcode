class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index, character in enumerate(haystack):
            if character == needle[0] and len(haystack[index:]) >= len(needle):
                if haystack[index:index + len(needle)] == needle:
                    return index
             
        return -1
        
        
if __name__ == '__main__':
    solution = Solution()
    haystack = 'sadbutsad' 
    needle = 'sad'
    print(solution.strStr(haystack=haystack, needle=needle))
    
    haystack = "leetcode"
    needle = "leeto"
    print(solution.strStr(haystack=haystack, needle=needle))
    
    haystack = 'mississippi'
    needle = 'issip'  
    print(solution.strStr(haystack=haystack, needle=needle))
    