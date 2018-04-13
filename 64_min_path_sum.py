class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # space O(m)
        m = len(grid)
        n = len(grid[0])

        cur = [grid[0][0]] + [0] * (m - 1)

        # initialize cur array
        for i in range(1, m):
            cur[i] = cur[i - 1] + grid[i][0]

        # go column by column
        for j in range(1, n):
            cur[0] += grid[0][j]
            for i in range(1, m):
                cur[i] = min(cur[i], cur[i - 1]) + grid[i][j]
        return cur[m - 1]

    def minPathSum2(self, grid):
        # space O(m*n)
        m = len(grid)
        n = len(grid[0])

        A = [[0 for j in range(n)] for i in range(m)]
        A[0][0] = grid[0][0]

        for i in range(1,m):
            A[i][0] = A[i-1][0] + grid[i][0]
        for j in range(1,n):
            A[0][j] = A[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                A[i][j] = min(A[i-1][j], A[i][j-1]) + grid[i][j]

        return A[-1][-1]





s = Solution()
s.minPathSum2([[1,3,1],[1,5,1],[4,2,1]])


