class Solution:
	def isValid(self, s: str) -> bool:
		l = 0
		while len(s) != l:
			l = len(s)
			s = s.replace('[]', '').replace('()', '').replace('{}', '')
		return bool(s) == False


s = Solution()
print(s.isValid('{}('))