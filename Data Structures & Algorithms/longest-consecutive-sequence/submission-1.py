class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_length = 0

        for num in hashset:
            if (num - 1) not in hashset:
                curr = 1
                while (num + curr) in hashset:
                    curr += 1

                max_length = max(max_length, curr)
        return max_length
