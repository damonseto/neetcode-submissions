class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def backtrack(path, index):
            if index == len(nums):
                self.res.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            backtrack(path, index + 1)
        backtrack([], 0)
        return self.res
        