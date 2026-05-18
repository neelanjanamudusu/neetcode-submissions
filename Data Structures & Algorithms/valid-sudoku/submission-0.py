class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sol = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    row = (num, i)
                    col = (j, num)
                    box = (i // 3, j // 3, num)
                    if row in sol or col in sol or box in sol:
                        return False
                    sol.add(row)
                    sol.add(col)
                    sol.add(box)
        return True