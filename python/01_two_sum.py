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
                first_index = nums.index(target - num)
                nums.remove(target - num)
                second_index = nums.index(num) + 1
                return [first_index, second_index]
            
            result.add(num)
        
        return None

    
if __name__ == '__main__':
    solution = Solution()
    target = 6
    nums = [3, 3]
    print(solution.twoSum(nums=nums, target=target))
    
    target = 9
    nums = [2, 7, 11, 15]
    print(solution.twoSum(nums=nums, target=target))
    
    target = 6
    nums = [3, 2, 4]
    print(solution.twoSum(nums=nums, target=target))
    