class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Find max island area
        # DFS
        # Iterate through 
        # reaches land then call dfs
        ## traverse until no more island
        ## store those indexes in dict


        islands = {}
        count = 0
        maxArea = 0

        def islandDFS(i, j):
            if i > len(grid) - 1 or j > len(grid[0]) - 1:
                return 0
            if i < 0 or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in islands:
                return 0

            islands[(i, j)] = 1

            return 1 + islandDFS(i + 1, j) + islandDFS(i - 1, j) + islandDFS(i, j + 1) + islandDFS(i, j - 1)
            


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    if (i, j) not in islands:
                        count += 1
                        maxArea = max(maxArea, islandDFS(i, j))


        return maxArea


        




        