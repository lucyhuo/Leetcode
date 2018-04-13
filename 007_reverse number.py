class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 1 if x > 0 else -1
        r = int(str(s*x)[::-1])
        return r * s * (r < 2 ** 31)