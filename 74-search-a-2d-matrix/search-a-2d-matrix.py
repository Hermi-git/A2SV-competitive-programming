class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for row in range(n):
            l = 0
            r = m-1

            while l <= r:
                mid = (l+r)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r = mid -1
                else:
                    l = mid+1
        return False

