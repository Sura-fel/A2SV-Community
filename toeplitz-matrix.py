class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for m in range(1, len(matrix)):
            for n in range(1, len(matrix[m])):
                if matrix[m][n] != matrix[m-1][n-1]:
                    return False
        return True
