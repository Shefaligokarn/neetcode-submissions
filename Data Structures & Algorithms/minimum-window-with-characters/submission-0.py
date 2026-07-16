class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        if not t:
            return ""
        need = defaultdict(int)
        window = defaultdict(int)


        for c in t: 
            need[c] += 1

        l = 0
        have = 0
        required = len(need)

        start =0
        best = float("inf")
        for r,c in enumerate(s):
            window[c] +=1
            if c in need and window[c] == need[c]:
                have += 1
            while have == required:
                if r-l+1 < best:
                    start = l
                    best = r-l+1
                left_char = s[l]
                window[left_char]-=1
                if (left_char in need and window[left_char] < need[left_char]):
                    have -= 1
                l += 1
        if best == float("inf"):
            return ""
            

        return s[start:start+best]