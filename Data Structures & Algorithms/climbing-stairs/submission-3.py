class Solution:
    def climbStairs(self, n: int) -> int:
        # DFS
        # Brute 
        # Explore every single possibility
        # Each recursive call explores both possibilities


        mem = {}

        def recursive_helper(step: int) -> None:
            if step > n:
                return 0
            elif step == n:
                return 1

            if step in mem:
                return mem[step]


            mem[step] = recursive_helper(step + 1) + recursive_helper(step + 2)

            return mem[step]


        return recursive_helper(0)


            




