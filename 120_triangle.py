class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        h = len(triangle)

        Res = triangle[-1]

        for l in range(h-2,-1,-1):
            for i in range(len(triangle[l])):
                Res[i] = min(Res[i], Res[i+1]) + triangle[l][i]
        return Res[0]

s=Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])


