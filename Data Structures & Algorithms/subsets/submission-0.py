class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # appending the current number

            subset.append(nums[i])
            dfs(i+1) 

            # removing the element the number we just added

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res