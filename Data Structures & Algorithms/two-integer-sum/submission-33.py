class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):            
            seen[val] = idx

        for idx, val in enumerate(nums):
            diff = target - val

            if diff in seen and seen[diff] != idx:
                return [min(seen[diff], idx), max(seen[diff], idx)]