class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        num_islands = 0
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num_islands += 1
                    search_queue = deque()
                    search_queue.append((row, col))
                    grid[row][col] = "0"
                    while search_queue:
                        curr_coords = search_queue.popleft() 
                        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                        for dir in dirs:
                            next_row = curr_coords[0] + dir[0]
                            next_col = curr_coords[1] + dir[1]
                            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == "1":
                                grid[next_row][next_col] = "0"
                                search_queue.append((next_row, next_col))

                
        return num_islands
