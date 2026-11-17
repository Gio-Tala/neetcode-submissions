class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS SEARCH
        # mark visited 1s as 0 so we don't revisit
        total_islands = 0
        search_stack = []


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    search_stack.append((row, col))
                    grid[row][col] = "0"
                    while search_stack:
                        (curr_row, curr_col) = search_stack.pop()
                        dirs = [(1,0), (-1,0), (0,1), (0, -1)]
                        for (r_dir, c_dir) in dirs:
                            new_r = curr_row + r_dir
                            new_c = curr_col + c_dir 
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                                if grid[new_r][new_c] == "1":
                                    search_stack.append((new_r, new_c))
                                    grid[new_r][new_c] = "0"
                                
                    total_islands += 1


        return total_islands