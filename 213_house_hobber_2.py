class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        return max(self.rob_base(nums[0:l - 1]), self.rob_base(nums[1:l]))

    def rob_base(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        pre, cur = 0, 0

        for i in range(l):
            temp = max(pre + nums[i], cur)
            pre = cur
            cur = temp

        return cur

s = Solution()
s.rob([1,1])