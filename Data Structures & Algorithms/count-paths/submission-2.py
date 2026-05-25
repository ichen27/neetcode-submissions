class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m rows, n columns
        # Top corner: grid[0][0]
        # Bottom Right: grid[m-1][n-1]
        count = 0


        def recursive_helper(down, right):
            nonlocal count

            if down == m-1 and right == n-1:
                count += 1
                return
            if down >= m or right >= n:
                return

            
            recursive_helper(down, right+1)
            
            recursive_helper(down+1, right)

            
            return


        recursive_helper(0, 0)
        return count