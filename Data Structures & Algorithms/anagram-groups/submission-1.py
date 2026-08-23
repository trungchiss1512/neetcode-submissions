from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for word in strs:
            decode = [0] * 26
            for c in word:
                decode[ord(c) - ord('a')] += 1
            key = tuple(decode)
            anagrams_dict[key].append(word)
        return list(anagrams_dict.values())
