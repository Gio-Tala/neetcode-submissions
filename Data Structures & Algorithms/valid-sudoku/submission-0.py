class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go column by column, row by row, square by square
        # for each col/row/square, create a set that tracks items
        # if we find an item alr in set, return false
        # repeat until false or until board cleared

        # rows
        for row in board:
            num_set = set()
            for num in row:
                if num in num_set and num != ".":
                    print("rows")
                    return False
                num_set.add(num)

        # columns
        for i in range(9):
            num_set = set()
            for j in range(9):
                curr_num = board[j][i]
                if curr_num in num_set and curr_num != ".":
                    print("cols")
                    return False
                num_set.add(curr_num)
            
        # squares
        for i in range(1,4):
            for j in range(1,4):
                num_set = set()
                for k in range(i*3 - 3, i*3):
                    for l in range(j*3 - 3, j*3):
                        curr_num = board[k][l]
                        if curr_num in num_set and curr_num != ".":
                            print(i,j)
                            print(curr_num, num_set)
                            print("squares")
                            return False
                        num_set.add(curr_num)

        return True
                        
