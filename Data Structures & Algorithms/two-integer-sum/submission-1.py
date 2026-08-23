class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in indices:
                indices[nums[i]] = i
            else:
                result = [indices[complement], i]
        return result
