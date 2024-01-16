class Solution:
    def addDigits(self, num):
        result = 0
        for item in str(num):
            result += int(item)
            
        if result >= 10:
            return self.addDigits(result)

        else:
            return int(result)

    
if __name__ == '__main__':
    solution = Solution()
    
    num = 38
    # print(solution.addDigits(num)) # 3 + 8 = 11, 1 + 1 = 2
    
    num = 19
    print(solution.addDigits(num)) # 1 + 9 = 10, 1 + 0 = 1
    