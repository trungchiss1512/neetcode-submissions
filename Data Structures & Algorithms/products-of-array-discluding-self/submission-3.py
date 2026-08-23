class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_list = [1] * len(nums)
        pre = 1
        for i in range(len(nums)-1):
            pre *= nums[i]
            pre_list[i+1] = pre
        
        suf_list = [1] * len(nums)
        suf = 1
        for i in range(len(nums)-1, 0, -1):
            suf *= nums[i]
            suf_list[i-1] = suf
        
        res = [pre_list[i] * suf_list[i] for i in range(len(pre_list))]
        return res