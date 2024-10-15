from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isgood(board, row, col, i):
            for j in board[row]:
                if j == str(i):
                    return False

            for j in range(9):
                if board[j][col] == str(i):
                    return False

            temprow = (row // 3) * 3
            tempcol = (col // 3) * 3

            for a in range(temprow, temprow + 3):
                for b in range(tempcol, tempcol + 3):
                    if board[a][b] == str(i):
                        return False

            return True

        dot = 0
        for line in board:
            for i in line:
                if i == ".":
                    dot += 1

        def help(board, row, col):

            if row == 9:
                return True

            nextrow = row
            nextcol = col

            if col == 9:
                return help(board, row + 1, 0)

            if board[row][col] != ".":
                return help(board, row, col + 1)

            for i in range(1, 10):
                if isgood(board, row, col, i):
                    board[row][col] = str(i)
                    if help(board, nextrow, nextcol):
                        return True
                    else:
                        board[row][col] = "."

        help(board, 0, 0)
