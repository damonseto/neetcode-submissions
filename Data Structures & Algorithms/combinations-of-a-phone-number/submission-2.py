class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        di = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",        
        }
        if digits == "":
            return []
        def bt(cur, i):
            if len(cur) == len(digits):
                res.append(cur[:])
                return
            for char in di[digits[i]]:
                bt(cur+char, i+1)

        bt("", 0)
        return res