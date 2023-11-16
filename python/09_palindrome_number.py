class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            Given an integer x, return true if x is a palindrome, and false otherwise.
        """
        y = x
        mod = 0
        length = 0
        result = 0
        while x > 0:
            mod = x % 10
            length = len(str(x))
            if x >= 10:
                result += mod * (10 ** (length - 1))
            else:
                result += mod * length 
            
            x = x // 10
        
        return result == y
    

if __name__ == '__main__':
    solution = Solution()
    
    x = 123
    print(solution.isPalindrome(x))
    