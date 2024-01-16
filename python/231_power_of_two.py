class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False 
        
        if n == 1:
            return True
        
        if n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n/2)
            

if __name__ == '__main__':
    solution = Solution()
    
    n = 1
    print(solution.isPowerOfTwo(n))
    
    n = 16
    print(solution.isPowerOfTwo(n))
    
    n = 0
    print(solution.isPowerOfTwo(n))
    
    n = -16
    print(solution.isPowerOfTwo(n))
