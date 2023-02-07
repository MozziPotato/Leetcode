class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 가로, 세로, 3x3 정사각형 총 3가지 경우의 수에 대해서 각각 9번씩 for문을 총 27번을 돌리는 접근법이 기본
        # 이 때는 1~9를 index로, index의 존재 여부 true & false로 나타내는 Hash Table을 사용
        
        output = True
        hash_table = {"1":1, "2":1, "3":1,"4":1,"5":1,"6":1,"7":1,"8":1,"9":1, ".":1}
        size = 9
        subsize = 3
        
        # 가로, 세로 체크
        for i in range(size):
            row_hash_table = copy.deepcopy(hash_table)
            col_hash_table = copy.deepcopy(hash_table)
            for j in range(size):
                row = board[i][j]
                col = board[j][i]
                if not all([row_hash_table[row], col_hash_table[col]]):
                    output = False
                else:
                    if row != ".":
                        row_hash_table[row] = 0
                    if col != ".":
                        col_hash_table[col] = 0
            
        
        # 작은 정사각형 체크
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_hash_table = copy.deepcopy(hash_table)
                for k in range(subsize):
                    for l in range(subsize):
                        value = board[i+k][j+l]
                        if not square_hash_table[value]:
                            output = False
                        else:
                            if value != ".":
                                square_hash_table[value] = 0
                        
        return output