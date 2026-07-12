class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            if s[i] not in s_hash:
                s_hash[s[i]] = 1
            else : 
                s_hash[s[i]] += 1
            if t[i] not in t_hash:
                t_hash[t[i]] = 1
            else : 
                t_hash[t[i]] += 1
        return t_hash == s_hash
        
        