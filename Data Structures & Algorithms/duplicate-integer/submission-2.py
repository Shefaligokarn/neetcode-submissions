class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set() # can use hashmap too
        for i in range(len(nums)):
            if nums[i] in count:
                return True
            else:
                count.add(nums[i])
        return False

        #  count = set()
        #  for i in range(len(nums)):
        #     if nums[i] in count:
        #         return True
        #     else:
        #         count.add(nums[i])
        #  return False