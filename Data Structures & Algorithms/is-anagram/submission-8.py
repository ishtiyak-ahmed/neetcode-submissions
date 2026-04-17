class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicts = {}
        dictt = {}

        for char in s:
            if char not in dicts:
                dicts[char] = 0
            dicts[char] += 1

        for char in t:
            if char not in dictt:
                dictt[char] = 0
            dictt[char] += 1
        
        if dicts == dictt:
            return True
        return False