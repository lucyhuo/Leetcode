class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [None] * n

        t[0], t[1] = 1, 2

        for i in range(3, n+1):
            t[i - 1] = t[i - 2] + t[i - 3]

        return t[n - 1]

s = Solution()

s.climbStairs(2)
s.climbStairs(4)