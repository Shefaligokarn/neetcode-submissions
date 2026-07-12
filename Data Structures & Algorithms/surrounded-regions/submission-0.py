class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        #1. identifying the un surrounded region
        #2. converting 0 into T
        #3. converting all the 0 into X 
        #4. converting all t back to o


        if not board:  # handle empty board case
            return
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != 'O'
            ):
                return
            board[r][c] = 'T'  # Mark 'O' as 'T' to avoid revisiting
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Start DFS from all 'O's on the border
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)

        # Flip all remaining 'O's to 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # Flip 'T's (temporary marks) back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
