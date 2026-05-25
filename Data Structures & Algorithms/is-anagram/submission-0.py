class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for key in s:

            if key in s_dict:
                s_dict[key] += 1
            else:
                s_dict[key] = 1

        for key in t:

            if key in t_dict:
                t_dict[key] += 1
            else:
                t_dict[key] = 1

        if s_dict == t_dict:
            return True
        else:
            return False
        