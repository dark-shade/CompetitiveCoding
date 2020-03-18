class Solution:
    def fib(self, N: int) -> int:
        # [F(0), F(1)]
        prev_nums = [0, 1]

        if N == 0:
            return prev_nums[0]

        elif N == 1:
            return prev_nums[1]
        else:
            for _ in range(2, N):
                new_sum = sum(prev_nums)
                prev_nums[0] = prev_nums[1]
                prev_nums[1] = new_sum
        
        return sum(prev_nums)

obj = Solution()
f = obj.fib(4)
print(f)