class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        self.res = False
        r = -1
        c = -1
        def backtrack(r, c, i) -> bool: 
            if word[i] != board[r][c]:
                return
            if i == len(word) - 1:
                self.res = True
                return
            seen.add((r,c))
            i = i + 1
            if c - 1 >= 0 and (r, c-1) not in seen:
                backtrack(r, c-1, i)
            if c + 1 < len(board[r]) and (r, c+1) not in seen:
                backtrack(r, c+1, i)
            if r - 1 >= 0 and (r-1, c) not in seen:
                backtrack(r-1, c, i)
            if r + 1 < len(board) and (r+1, c) not in seen:
                backtrack(r+1, c, i)
            seen.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[r])):
                backtrack(r, c, 0)
                
        return self.res

            
        