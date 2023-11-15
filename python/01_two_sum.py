from typing import List


class Solution:
    """
        Given an array of integers nums and an integer target, return indices of the two 
        numbers such that they add up to target.
    """
    def twoSum(self, nums: set[int], target: int) -> List[int]:
        result = set()
        for num in nums:
            if target - num  in result:
                return [nums.index(target - num), nums.index(num)]
            
            result.add(num)
        
        return None

    
if __name__ == '__main__':
    solution = Solution()
    target = 9
    nums = [2, 7, 11, 15]
    print(solution.twoSum(nums=nums, target=target))
    
    target = 6
    nums = [3, 2, 4]
    print(solution.twoSum(nums=nums, target=target))
    