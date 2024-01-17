class Solution:
    def summaryRanges(self, nums):
        ranges = []
        for num in nums:
            if not ranges or num > ranges[-1][1] + 1:
                ranges.append([num, num])
            else:
                ranges[-1][1] = num
                
        return [str(interval[0]) + '->' + str(interval[1]) if interval[0] != interval[1] else str(interval[0]) for interval in ranges]


if __name__ == '__main__':
    solution = Solution()
    
    nums = [0, 1, 2, 4, 5, 7]
    print(solution.summaryRanges(nums))
    