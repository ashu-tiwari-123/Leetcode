s = "anagram"
t = "nagaram"

def anagram():
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)