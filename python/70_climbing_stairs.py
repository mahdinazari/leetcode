class Solution(object):
    """
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    def climbStairs(self, n):
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[n]
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(5))
    