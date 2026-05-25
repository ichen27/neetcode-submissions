class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 step: 1
        # 2 steps: 2
        # 3 steps: 3
        # 4 steps: 5

        mem = {}

        def helper(i):
            if i == 1:
                return 1
            if i == 2:
                return 2

            if i in mem:
                return mem[i]

            total =  helper(i-1) + helper(i-2)

            mem[i] = total

            return total

        

        return helper(n)