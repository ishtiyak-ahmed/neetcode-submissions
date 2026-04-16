class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(min(i,j))
                    result.append(max(i,j))
                    return result