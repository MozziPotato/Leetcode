class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        height = len(board)
        width = len(board[0])

        top_side = [(0, i) for i in range(width)]
        bottom_side = [(height - 1, i) for i in range(width)]
        left_side = [(i, 0) for i in range(height)]
        right_side = [(i, width - 1) for i in range(height)]

        survived_coord = list()

        # function: "O"가 식별된 coordinate에 대해 DFS를 수행하여 Survived "O"을 식별
        def dfs(board: list[list[str]], i, j) -> None:

            survived_coord.append((i, j))
            
            # up
            if i > 0:
                dfs(board, i - 1, j) if board[i - 1][j] == "O" and (i - 1, j) not in survived_coord else None
            # down
            if i < height - 1:
                dfs(board, i + 1, j) if board[i + 1][j] == "O" and (i + 1, j) not in survived_coord else None
            # left
            if j > 0:
                dfs(board, i, j - 1) if board[i][j - 1] == "O" and (i, j - 1) not in survived_coord else None
            if j < width - 1:
                dfs(board, i, j + 1) if board[i][j + 1] == "O" and (i, j + 1) not in survived_coord else None

            

        # 윗변 DFS
        for (i, j) in top_side:
            if board[i][j] == "O" and (i, j) not in survived_coord:
                dfs(board, i, j)

        # 아랫변 DFS
        for (i, j) in bottom_side:
            if board[i][j] == "O" and (i, j) not in survived_coord:
                dfs(board, i, j)

        # 좌변 DFS
        for (i, j) in left_side:
            if board[i][j] == "O" and (i, j) not in survived_coord:
                dfs(board, i, j)

        # 우변 DFS
        for (i, j) in right_side:
            if board[i][j] == "O" and (i, j) not in survived_coord:
                dfs(board, i, j)

        for row in range(height):
            for col in range(width):
                if board[row][col] == "O" and (row, col) not in survived_coord:
                    board[row][col] = "X"
        