class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if (target <= row[-1]) and (target >= row[0]):
                low = 0
                high = len(row) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        low = mid +1 
                    else:
                        high = mid - 1
        return  False