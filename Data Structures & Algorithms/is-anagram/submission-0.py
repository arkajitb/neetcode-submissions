class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for val in s:
            if val not in s_dict:
                s_dict[val] = 1
            else:
                s_dict[val] += 1
        for val in t:
            if val not in t_dict:
                t_dict[val] = 1
            else:
                t_dict[val] += 1
        return s_dict == t_dict

