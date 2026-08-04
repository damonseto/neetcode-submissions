class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 1
        wrongCount = 0
        current = s[0]
        max = 0
        counter = 0
        while i < len(s):
            if counter > max:
                max = counter
            if s[i] != current:
                if k == 1:
                    first = i
                if wrongCount + 1 > k:
                    i = first
                    current = s[i]
                    counter = 0
                    wrongCount = 0
                elif wrongCount == 0:
                    first = i
                    wrongCount += 1
                    counter += 1
                else:
                    wrongCount += 1
                    counter += 1
            counter += 1
            i += 1
        return max
                
                
                

            
        