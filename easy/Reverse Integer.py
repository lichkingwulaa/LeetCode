class Solution:
	def reverse(self, x: int) -> int:
		num = int(str(x)[::-1].rstrip('-'))
		if x < 0: num *= -1
		return num if -2**31 < num < 2**31 - 1 else 0

s = Solution()
print(s.reverse(1534236469))