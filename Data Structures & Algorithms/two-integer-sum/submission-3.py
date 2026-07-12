class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashsets = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashsets:
                return[hashsets[diff],i]
            hashsets[n] = i   