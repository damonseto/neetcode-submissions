class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start = 0
        end = 1
        subs = ""
        max = 0
        for i in range(0, len(s)):
            temp = s[i:i + 1]
            if temp in subs:
                index = subs.find(temp)
                subs = subs[index + 1:len(subs)]
                subs += temp
            else:
                subs += temp
                if len(subs) > max:
                    max = len(subs)
        return max
        