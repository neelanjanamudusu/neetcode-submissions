from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while strs:
            first = strs[0]
            group = [first]
            for word in strs[1:]:
                if Counter(first) == Counter(word):
                    group.append(word)
            for word in group:
                strs.remove(word)
            result.append(group)
        return result