class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n > m:
            return False
        
        seen={}
        for i in range(n):
            seen[s1[i]]=1+seen.get(s1[i],0)

        for i in range(m - n + 1):
            window = {}
            for char in s2[i : i + n]:
                window[char] = 1 + window.get(char, 0)
            if window == seen:
                return True
        
        return False