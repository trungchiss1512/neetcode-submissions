class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lb, rb = 0,len(numbers)-1
        while numbers[lb] + numbers[rb] != target:
            if numbers[lb] + numbers[rb] > target:
                rb -= 1
            else:
                lb += 1
        return [lb+1,rb+1]