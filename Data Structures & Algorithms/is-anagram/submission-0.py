class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False
        freq1 = {}
        freq2 = {}
        for i in range ( m ):
            freq1[s[i]] = freq1.get(s[i],0) + 1 
            freq2[t[i]] = freq2.get(t[i],0) + 1 

        for char , val in freq1.items():

            if freq2.get(char,0) != val:
                return False
            
        return True