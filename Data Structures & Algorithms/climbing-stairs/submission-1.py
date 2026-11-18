class Solution:
    def climbStairs(self, n: int) -> int:
        # for each stair, there's 2 ways to get there: 
        # 1) stair right (1) before 2) stair 2 before
        hashed_ways = {}
        def num_ways(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n not in hashed_ways:
                hashed_ways[n] = num_ways(n-1) + num_ways(n-2)
            return hashed_ways[n]
        return num_ways(n)