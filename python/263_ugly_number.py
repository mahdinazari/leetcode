class Solution:
    """
        An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
    """
    def isUgly(self, n):
        if n <= 0:
            return False
        
        uglies = [2, 3, 5]
        for ugly in uglies:
            while n % ugly == 0:
                n = n / ugly
        
        return n == 1
        
        
if __name__ == '__main__':
    solutioin = Solution()
    
    n = 8
    print(solutioin.isUgly(n))
    
    n = 6
    print(solutioin.isUgly(n))
    
    n = 14
    print(solutioin.isUgly(n))
    
    n = 16
    print(solutioin.isUgly(n))
    