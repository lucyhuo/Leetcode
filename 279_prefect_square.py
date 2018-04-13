import math

class Solution:
    dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = self.dp + [math.inf] * n
        sqr = [i*i for i in range(1, int(math.sqrt(n))+1)]

        if math.sqrt(n) == int(math.sqrt(n)):
            return 1




        for i in range(1, n + 1):

            for j in sqr:
                if i - j < 0:
                    break
                self.dp[i] = min(self.dp[i - j] + 1, self.dp[i])

        return self.dp[n]


    def numSquares_bfs(self, n):
        sqr = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        visit = [0] * n
        Q1 = [n]
        Q2 = []
        level = 1
        while Q1:

            for i in range(len(Q1)):

                if math.sqrt(Q1[i]) == int(math.sqrt(Q1[i])):
                    return level

                for j in sqr:
                    if j > Q1[i]:
                        break
                    v = Q1[i] - j
                    if visit[v] == 1:
                        continue
                    Q2.append(v)
                    visit[v] = 1
            Q1 = Q2
            Q2 = []
            level += 1

        return level-1

s = Solution();
s.numSquares_bfs(12)