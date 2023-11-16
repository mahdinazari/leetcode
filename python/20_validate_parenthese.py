class Solution:
    """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    """
    def isValid(self, s: str) -> bool:
        pair = dict(('()', '[]', '{}'))
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif len(st) == 0 or x != pair[st.pop()]:
                return False
        return len(st) == 0
        
        
if __name__ == '__main__':
    solution = Solution()
    s = "(()[]){}"
    print(solution.isValid(s))
    