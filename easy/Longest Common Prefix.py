class Solution:
	def longestCommonPrefix(self, strs):
		if not strs: return ""
		ss = list(map(set, zip(*strs)))
		res = ""
		for x in ss:
			x = list(x)
			if len(x) > 1:
				break
			res = res + x[0]
		return res


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))

print(s.longestCommonPrefix(["dog","racecar","car"]))

print(s.longestCommonPrefix(['a']))