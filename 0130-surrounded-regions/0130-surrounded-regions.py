class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # boarder에 닿지 않으면 X에 둘러쌓일 수 밖에 없다.
        # 따라서 boarder에 닿아있는 O와 아닌 O를 식별한 후, flipped 처리할 수 있겠다.
        # boarder만 순차적으로 탐색하면서 O를 찾아냈을 때, BFS를 사용해서 연결된 O를 모두 찾아낸다. -> survived O
        # survived O를 표시할 O_board를 하나 더 생성해둬야 한다.
        # original board를 탐색하면서, O를 발견했을 때, O_board에 표기되어있지 않으면 flip 해버린다.
        
        M = len(board)
        N = len(board[0])
        O_board = [["X" for i in range(N)] for i in range(M)]
        
#         def BFS(queue):
            
#             while queue:
#                 visit = queue.popleft()
#                 i = visit[0]
#                 j = visit[1]
#                 O_board[i][j] = 'O'
                
#                 # 시계방향으로 append
#                 # top
#                 if i > 0:
#                     if board[i-1][j] == 'O' and O_board[i-1][j] == 'X':
#                         queue.append((i-1,j))
#                 # right
#                 if j < N - 1:
#                     if board[i][j+1] == 'O' and O_board[i][j+1] == 'X':
#                         queue.append((i, j + 1))
#                 # bottom
#                 if i < M - 1:
#                     if board[i+1][j] == 'O' and O_board[i+1][j] == 'X':
#                         queue.append((i+1, j))
#                 # left
#                 if j > 0:
#                     if board[i][j-1] == 'O' and O_board[i][j-1] == 'X':
#                         queue.append((i, j - 1))
                    
#         # 윗변, 아랫변 탐색
#         for i in range(N):
#             if board[0][i] == 'O' and O_board[0][i] == 'X':
#                 BFS(deque([(0,i)]))
#             if board[M-1][i] == 'O' and O_board[M-1][i] == 'X':
#                 BFS(deque([(M-1,i)]))
                
#         # 좌변, 우변 탐색
#         for i in range(M):
#             if board[i][0] == 'O' and O_board[i][0] == 'X':
#                 BFS(deque([(i,0)]))
#             if board[i][N-1] == 'O' and O_board[i][N-1] == 'X':
#                 BFS(deque([(i,N-1)]))
            
#         # Flip        
#         for i in range(M):
#             for j in range(N):
#                 if board[i][j] == 'O' and O_board[i][j] == 'X':
#                     board[i][j] = 'X'
                    
    
    
        # BFS에서 Time Limit Exceeded 발생 (Case 55/58)
        # DFS로 선회
    
    
        def DFS(i: int, j: int):
            
            O_board[i][j] = 'O'
                        
            # top
            if i > 0:
                if board[i-1][j] == 'O' and O_board[i-1][j] == 'X':
                    DFS(i-1,j)
            # right
            if j < N - 1:
                if board[i][j+1] == 'O' and O_board[i][j+1] == 'X':
                    DFS(i, j + 1)
            # bottom
            if i < M - 1:
                if board[i+1][j] == 'O' and O_board[i+1][j] == 'X':
                    DFS(i+1, j)
            # left
            if j > 0:
                if board[i][j - 1] == 'O' and O_board[i][j-1] == 'X':
                    DFS(i, j - 1)
                    
        # 윗변, 아랫변 탐색
        for i in range(N):
            if board[0][i] == 'O' and O_board[0][i] == 'X':
                DFS(0, i)
            if board[M-1][i] == 'O' and O_board[M-1][i] == 'X':
                DFS(M-1, i)
                
        # 좌변, 우변 탐색
        for i in range(M):
            if board[i][0] == 'O' and O_board[i][0] == 'X':
                DFS(i, 0)
            if board[i][N-1] == 'O' and O_board[i][N-1] == 'X':
                DFS(i, N-1)
            
        # Flip        
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O' and O_board[i][j] == 'X':
                    board[i][j] = 'X'