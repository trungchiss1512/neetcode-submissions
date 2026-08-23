class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in ordered:
                ordered[sorted_word] = []
            ordered[sorted_word].append(word)
        return list(ordered.values())