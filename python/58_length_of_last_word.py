class Solution:
    """
        Given a string s consisting of words and spaces, return the length of the last word in the string.
        A word is a maximal substring consisting of non-space characters only.
    """
    def lengthOfLastWord(self, s: str) -> int:
        words_list = s.split(' ')
        while '' in words_list:
            words_list.remove('')
        
        result = list(reversed(words_list))[0]
        return len(result)
        
        
if __name__ == '__main__':
    solution = Solution()
    s = "Hello World"
    print(solution.lengthOfLastWord(s)) # 5
    
    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s)) # 4
    
    s = "luffy is still joyboy"
    print(solution.lengthOfLastWord(s)) # 6
    