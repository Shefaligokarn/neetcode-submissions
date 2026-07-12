class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_long = set(nums)
        max_long = 0

        for i in (nums):
            if i - 1 not in hash_long:
                current = 0
                while i + current in hash_long:
                    current += 1
                max_long = max(current, max_long)
        return max_long
