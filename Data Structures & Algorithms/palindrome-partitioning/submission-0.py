class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(cur, j, i):
            if i >= len(s):
                if j == i:
                    res.append(cur[:])
                return
            if isPalindrome(s[j:i+1]):
                cur.append(s[j:i+1])
                backtrack(cur, i+1, i+1)
                cur.pop()
            backtrack(cur, j, i+1)

        def isPalindrome(s: str) -> bool:
            l = 0
            r = len(s) - 1
            if s == "":
                return True
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        backtrack([], 0, 0)
        return res