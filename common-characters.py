class Solution:
 def charFrequency(self, word):
   f = [0 for i in range(26)]
   for ch in word:
       f[ord(ch) - ord('a')] += 1
   return f


 def commonChars(self, words):
   min_frequency = self.charFrequency(words[0])
   for word in words:
       frequency = self.charFrequency(word)
       for i in range(26):
           if frequency[i] < min_frequency[i]:
               min_frequency[i] = frequency[i]
   result = []
   for i in range(26):
       result.extend([chr(97 + i)] * min_frequency[i])


   return result

a = Solution()

print(a.commonChars(["bella","label","roller"]))
