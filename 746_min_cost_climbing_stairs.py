class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1:
            return cost[0]
        t = [None] * len(cost)
        t[0], t[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            t[i] = min(t[i - 1] + cost[i], t[i - 2] + cost[i])
        return min(t[-1],t[-2])
s = Solution()
s.minCostClimbingStairs([10, 15, 20])