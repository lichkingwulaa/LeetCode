S = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
class Solution:
	def romanToInt(self, s: str) -> int:
		num = 0
		for i in range(len(s) - 1):
			if S[s[i]] >= S[s[i + 1]]:
				num += S[s[i]]
			else:
				num -= S[s[i]]
		return num + S[s[-1]]


s = Solution()
print(s.romanToInt('IX'))