class Solution:
    def helper(self, nums, res, subset, i ):
        #base case
        if len(subset) >= len(nums):
            return
        
        # for loop
        for a in range(i, len(nums)):
            subset.append(nums[a])
            res.append(subset.copy())        
            self.helper(nums, res, subset, a+1 )
            subset.pop()
            # print(subset)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        self.helper(nums, res, [], 0 )
        return res
        
        

        

    
        
    





        
