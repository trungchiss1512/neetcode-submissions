class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1
        frequency_list = [(n,f) for n,f in frequency.items()]
        sorted_frq_list = sorted(frequency_list, key=lambda x: x[1], reverse = True)
        return [a[0] for a in sorted_frq_list[:k]]
