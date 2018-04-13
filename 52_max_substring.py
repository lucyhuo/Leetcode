class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # subproblem: a[i] is the max sum of the array ending at i
        # compare the current maxsum with the maxsum we have ever seen so far

        current_max = overall_max = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            overall_max = max(overall_max, current_max)
        return overall_max

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])