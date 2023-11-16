from audioop import reverse


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            Given an integer x, return true if x is a palindrome, and false otherwise.
        """
        n = x
        reverse = 0
        while n > 0:
            mod = n % 10 
            n = n // 10 
            reverse = reverse * 10 + mod 
        
        return x == reverse
        

if __name__ == '__main__':
    solution = Solution()
    
    x = 121
    print(solution.isPalindrome(x))
    