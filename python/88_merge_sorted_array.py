from typing import List



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
        and two integers m and n, representing the number of elements in nums1 and nums2 
        respectively.
        """
        result = sorted(nums1[:m] + nums2[:n])
        nums1[:] = []

        for i in result:
            nums1.append(i)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(solution.merge(nums1=nums1, m=m, nums2=nums2, n=n)) # [1,2,2,3,5,6]
    
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(solution.merge(nums1=nums1, m=m, nums2=nums2, n=n)) # [1]
    
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(solution.merge(nums1=nums1, m=m, nums2=nums2, n=n)) # [1]
    