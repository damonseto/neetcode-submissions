class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, o, c):
            if len(path) >= n * 2:
                res.append(path[:])
                return
            if o == n:
                path += ")"
                backtrack(path, o, c + 1)
            elif o <= c:
                path += "("
                backtrack(path, o + 1, c)
            else:
                path += "("
                backtrack(path, o + 1, c)
                path = path[:-1]
                path += ")"
                backtrack(path, o, c + 1)
        backtrack("", 0, 0)
        return res
            
            
        