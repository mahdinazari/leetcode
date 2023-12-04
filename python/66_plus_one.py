from typing import List


class Solution:
    """
        You are given a large integer represented as an integer array digits, where each digits[i] is the
        ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.
        The large integer does not contain any leading 0's.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for index, digit in enumerate(reversed(digits)):
            total += digit * (10 ** index)
            
        result = list(str(total + 1))
        return [int(r) for r in result]
        
        
if __name__ == '__main__':
    solution = Solution()
    digits = [1, 2, 3]
    print(solution.plusOne(digits))
    
    digits = [4, 3, 2, 1]
    print(solution.plusOne(digits))
    
    digits = [9]
    print(solution.plusOne(digits))
    
    digits = [9, 9]
    print(solution.plusOne(digits))
    