class Solution(object):
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def backtrack(index):

            nonlocal complete

            if index == len(free_cells):
                complete = True
                return

            #FIND CURRENT EMPTY POSITION
            r_c, c_c = free_cells[index]
            #test all possible numbers
            for d in range(9):
                #check if the digit is used in that r/c. The r/c has all possible digits marked T?F if it is there or not. If it is in that places r,c or box it cannot be put in the board in that location.
                if (not r_used[r_c][d] and not c_used[c_c][d] and not box_used[r_c//3][c_c//3][d]):
                    r_used[r_c][d] = True
                    c_used[c_c][d] = True
                    box_used[r_c//3][c_c//3][d] = True

                    board[r_c][c_c] = str(d+1)

                    #recursion to solve next
                    backtrack(index + 1)

                    if complete:
                        return

                    r_used[r_c][d] = False
                    c_used[c_c][d] = False
                    box_used[r_c//3][c_c//3][d] = False

        #INITIALIZE
        r_used = [[False] * 9 for _ in range(9)]
        #r_used[i][j] = True if j+1 is used in row i
        c_used = [[False] * 9 for _ in range(9)]
        #r_used[i][j] = True if j+1 is used in column i
        box_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        #r_used[box_ri][box_ci][j] = True if d is used in box i

        #stores empties
        free_cells = []
        #stores boolean value for if solved
        complete = False

        #START/SET UP EMPTIES
            #r is the index of rows, c is index of columns
        for r_c in range(9):
            for c_c in range(9):
                if board[r_c][c_c] == '.':
                    #record empties position in tuple in list
                    free_cells.append((r_c, c_c))
                else:
                    #[i][j] is a digit 1-9
                    d = int(board[r_c][c_c])-1 #because on board it is +1
                    #set already there r,c and box to true
                    r_used[r_c][d] = True
                    c_used[c_c][d] = True
                    box_used[r_c//3][c_c//3][d] = True
        backtrack(0)

