class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in strs:
            encoded += str(len(i)) + '#' + i
            print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            len_s = int(s[i:j])
            decoded.append(s[j+1:j+len_s+1])
            i = j + len_s + 1
        return decoded

