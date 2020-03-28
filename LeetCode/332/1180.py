class Solution:
    def countLetters(self, S: str) -> int:
        curr_ch = ""
        substrings = []
        cnt = 0

        for ch in S:
            if len(curr_ch) == 0:
                curr_ch = ch
                continue
            if ch in curr_ch:
                curr_ch += ch
            else:
                substrings.append(curr_ch)
                curr_ch = ch

        substrings.append(curr_ch)

        for subs in substrings:
            n = len(subs)
            cnt += n + (n * (n - 1) / 2)
        
        return int(cnt)

obj = Solution()
cnt = obj.countLetters("aaaba")
print(cnt)