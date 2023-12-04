from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            Given a sorted array of distinct integers and a target value, return the index if the 
            target is found. If not, return the index where it would be if it were inserted in order.
        """
        for index, num in enumerate(nums):
            if target <= nums[0]:
                return 0
            
            if target > nums[len(nums) - 1]:
                return len(nums)
            
            if target >= num:
                if len(nums) > index + 1:
                    if target < nums[index + 1]:
                        return(index + 1) if target > num else index
                
                else:
                    return(index) if target > num else index


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 3, 5, 6]
    target = 2 
    print(solution.searchInsert(nums=nums, target=target)) # 1
    
    nums = [1, 3, 5, 6]
    target = 5 
    print(solution.searchInsert(nums=nums, target=target)) # 2
    
    nums = [1, 3, 5, 6]
    target = 7
    print(solution.searchInsert(nums=nums, target=target)) # 4
    
    nums = [1, 3, 5, 6]
    target = 0 
    print(solution.searchInsert(nums=nums, target=target)) # 0
    
    nums = [1, 3]
    target = 3
    print(solution.searchInsert(nums=nums, target=target)) # 1
    