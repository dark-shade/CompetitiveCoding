"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        final_Str = S

        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                if len(S) > i:
                    final_Str = self.removeDuplicates(S[:i-1] + S[i+1:])
                    break
                else:
                    return ""

        return final_Str
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for ch in S:
            if stack:
                prev = stack.pop()
                if prev == ch:
                    continue
                stack.append(prev)
            stack.append(ch)

        return "".join(stack)
        