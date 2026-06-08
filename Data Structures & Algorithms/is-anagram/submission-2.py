class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen1=list(s)
        seen2=list(t)
        seen1.sort()
        seen2.sort()
        x=seen1
        y=seen2
        if x==y:
            return True
        else:
            return False