class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: Dict = collections.defaultdict(set)
        cols: Dict = collections.defaultdict(set)
        boxes: Dict = collections.defaultdict(set)
        for (r,row) in enumerate(board):
            for (c,val) in enumerate(board[r]):
                if val == ".":
                    print("c:",c,"r:",r,"row:",row, "val:",val)
                    continue
                elif(
                        val in rows[r] or 
                        val in cols[c] or 
                        val in boxes[(r//3, c//3)]
                    ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        return True
