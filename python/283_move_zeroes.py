class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        Note that you must do this in-place without making a copy of the array.
        """
        index = 0
        counter = 0
        while counter < len(nums) -1:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
            
            else:
                index += 1
            
            counter += 1
                

if __name__ == '__main__':
    solution = Solution()
    
    nums = [0,1,0,3,12]
    # solution.moveZeroes(nums=nums)
    print(nums)

    nums = [0,0,1]
    solution.moveZeroes(nums=nums)
    print(nums)