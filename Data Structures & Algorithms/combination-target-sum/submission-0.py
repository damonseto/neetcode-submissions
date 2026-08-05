class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, start):
            if path in res:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) >= target:
                return
            for i in range(start, len(nums)):
                temp = path[:]
                temp.append(nums[i])
                backtrack(temp, i)
                temp.pop()
        backtrack([], 0)
        return res