class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:param: str
		:return: int
		"""
		cur = ''
		num = [0]
		for x in s:
			if x not in cur:
				cur += x
			else:
				num.append(len(cur))
				cur = cur[cur.index(x) + 1:] + x
		return max(num + [len(cur)])

solu = Solution()
print(solu.lengthOfLongestSubstring(""))