class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_cell(square):
            row_from_bottom = (square-1)//n
            col = (square-1)%n
            if row_from_bottom %2 == 1:
                col = n - 1 - col
            row = n - 1 - row_from_bottom
            return row, col

        q = deque([(1, 0)])
        visited = {1}
        while q:
            curr, moves = q.popleft()
            if curr == n**2:
                return moves
            for die in range(curr+1, min(curr+6, n**2)+1):
                r, c = get_cell(die)
                next_square = die

                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
        return -1






        