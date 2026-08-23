class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        numsSet = set(nums)
        beginners = {}
        for num in nums:
            if (num-1) in numsSet:
                continue
            
            beginners[num] = 0
            for i in range(len(numsSet)):
                if (num+i) not in numsSet:
                    break
                beginners[num] += 1

        return max(beginners.values())