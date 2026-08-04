class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        inner = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) - 1]:
                inner = mid
                break
            if target > matrix[mid][0]:
                lo = mid + 1
            else:
                hi = mid - 1
        lo = 0
        hi = len(matrix[inner])
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[inner][mid] == target:
                inner = mid
                return True
            if target > matrix[inner][mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
            