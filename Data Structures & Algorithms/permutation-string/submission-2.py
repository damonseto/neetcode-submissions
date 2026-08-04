class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        if len(s1) > len(s2):
            return False
        for char in s1:
            if char not in need:
                need[char] = 0
            need[char] += 1
        
        l = 0
        r = len(s1)
        while r <= len(s2):
            check = {}
            temp = s2[l:r]
            for char in temp:
                if char not in check:
                    check[char] = 0
                check[char] += 1
            if check == need:
                return True
            l += 1
            r += 1
        return False

        

        