class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        height = len(matrix)
        width = len(matrix[0])
        coordinates = list()
        
        for i in range(height):
            for j in range(width):
                value = matrix[i][j]
                if not value:
                    coordinates.append([i,j])
        
        for coordinate in coordinates:
            for i in range(height):
                matrix[i][coordinate[1]] = 0
            for j in range(width):
                matrix[coordinate[0]][j] = 0
                    