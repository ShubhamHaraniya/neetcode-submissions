class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row,col = len(matrix),len(matrix[0])
        low,high = 0,row*col-1

        while low <= high:
            mid = (low+high) // 2

            r,c = mid // col, mid % col

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False