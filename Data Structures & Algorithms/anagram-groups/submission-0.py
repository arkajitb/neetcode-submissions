from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for s in strs:
            strs_dict[tuple(sorted(s))].append(s)
        
        return list(strs_dict.values())