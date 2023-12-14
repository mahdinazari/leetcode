from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # https://leetcode.com/problems/contains-duplicate-ii/
        """
            Given an integer array nums and an integer k, return true if there are two distinct indices
            i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
        """
        lookup = {}
        for index, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = index
            else:
                if index - lookup[num] <= k:
                    return True
                
                lookup[num] = index

        return False
        

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(solution.containsNearbyDuplicate(nums=nums, k=k)) # True
    
    nums = [1, 0, 1, 1]
    k = 1
    print(solution.containsNearbyDuplicate(nums=nums, k=k)) # True
    
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(solution.containsNearbyDuplicate(nums=nums, k=k)) # False
