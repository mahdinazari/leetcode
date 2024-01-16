class Solution:
    def isAnagram(self, s, t):
        for char in t:
            if char not in s or (t.count(char)) > s.count(char) or len(t) < len(s):
                return False
        
        return True
    
        
if __name__ == '__main__':
    solutuin = Solution()
    t = 'anagram'
    s = 'nagaram'
    # print(solutuin.isAnagram(t=t, s=s)) # True
    
    t = 'car'
    s = 'cat'
    # print(solutuin.isAnagram(t=t, s=s)) # False
    
    s = 'rat'
    t = 'car'
    # print(solutuin.isAnagram(t=t, s=s)) # False
    
    s = 'ab'
    t = 'a'
    print(solutuin.isAnagram(t=t, s=s)) # False
