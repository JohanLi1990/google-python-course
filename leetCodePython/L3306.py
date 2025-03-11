class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # sliding windows
        # open the window up to include more chars
        def isVowel(c):
            return c in ['a', 'e', 'i', 'o', 'u']
        
        vowels={}
        j, ans= 0, 0
        resonant = 0
        nextResonant = [0 for i in range(len(word))]
        nextR = len(word)
        for i in range(len(word) - 1, 0, -1):
            nextResonant[i] = nextR
            if (not isVowel(word[i])):
                nextR = i
            
        for i in range(len(word)):
            if isVowel(word[i]):
                vowels[word[i]] = vowels.get(word[i], 0) + 1
            else:
                resonant += 1 
            while resonant > k:
                if isVowel(word[j]):
                    vowels[word[j]] -= 1
                    if (vowels[word[j]] == 0):
                        vowels.pop(word[j])
                else:
                    resonant -= 1
                if len(vowels.keys()) == 5:
                    ans += 1
                j += 1

            while len(vowels.keys()) == 5 and resonant == k:
                ans += nextResonant[i] - i
                if isVowel(word[j]):
                    vowels[word[j]] -= 1
                    if (vowels[word[j]] == 0):
                        vowels.pop(word[j])
                else:
                    resonant -= 1
                j += 1 
        
        return ans
    
soln = Solution()
print(soln.countOfSubstrings("aeioqq", 1))  # 0
print(soln.countOfSubstrings("ieaouqqieaouqq", 1)) # 3
print(soln.countOfSubstrings("ieaouquqieaouqq", 1)) # 6
print(soln.countOfSubstrings("aeiou", 0)) # 1
print(soln.countOfSubstrings("iqeaouqi", 2)) # 3
print(soln.countOfSubstrings("aoaiuefi", 1)) # 4
        