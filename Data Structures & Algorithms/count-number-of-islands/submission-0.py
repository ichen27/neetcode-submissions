class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Traverse the grid
        ## Aware of edge cases
        ## Traverse each node once
        # Count when reaches new land
        
        # Set edges for recusive function
        row_tot = len(grid)
        col_tot = len(grid[0])

        land = []
        count = 0

        # Recursive Function to traverse connected land

        def traverse(coord):
            # traverse up, down, left, right
            # Stay within edges
            # (4, 5)
            nonlocal land
            row, col = coord
            print(f"({row},{col})")

            j = ""
            for i in land:
                j = j + str(i)

            print(f"Passed: {j}")


            if row < row_tot - 1: # if can move to top and botton row
                row1 = row + 1 # Move Down
                if grid[row1][col] == "1" and (row1,col) not in land: # if its land thats not already passed
                    print(f"Down from ({row},{col})")
                    land.append((row1,col)) # append to land
                    traverse((row1, col)) # Traverse up
                else:
                    print(f"Can't Move down from ({row},{col}) to ({row1},{col})")
            if row > 0:
                row2 = row - 1 # Move Up
                if grid[row2][col] == "1" and (row2,col) not in land:
                    print(f"Up from ({row},{col})")
                    land.append((row2,col))
                    traverse((row2, col)) # Traverse down
                else:
                    print(f"Can't Move Up from ({row},{col}) to ({row2},{col})")

            if col < col_tot - 1: # if can move to the furthest outer edges
                col1 = col + 1
                if grid[row][col1] == "1" and (row,col1) not in land:
                    print(f"Right from ({row},{col})")
                    land.append((row,col1))
                    traverse((row,col1))
                else:
                    print(f"Can't Move Right from ({row},{col}) to ({row},{col1})")
            if col > 0:
                col2 = col - 1
                if grid[row][col2] == "1" and (row,col2) not in land:
                    print(f"Left from ({row},{col})")
                    land.append((row,col2))
                    traverse((row,col2))
                else:
                    print(f"Can't Move Left from ({row},{col}) to ({row},{col2})")

            return

        # Grid Traversal
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                # If hits land, traverse entire island before continuing
                # DFS/BFS
                # Recusion
                # keep track of land we've travelled already
                if (x, y) not in land:

                    if grid[x][y] == "1":
                        # Call recusion function
                        print("New Island")
                        count += 1
                        traverse((x,y))
        return count

        
        