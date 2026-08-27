class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    row_key = f"{val} in row {r}"
                    col_key = f"{val} in col {c}"
                    box_key = f"{val} in box {r//3}-{c//3}"

                    if row_key in seen or col_key in seen or box_key in seen:
                        return False

                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)

        return True