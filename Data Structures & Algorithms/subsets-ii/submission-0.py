class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(path, index):
            if index == len(nums):
                res.append(path[:])
                return
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            while index < len(nums) - 1 and nums[index] == nums[index+1]:
                index += 1
            backtrack(path, index + 1)
        backtrack([], 0)
        return res

            
        