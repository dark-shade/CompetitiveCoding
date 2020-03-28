class Solution:
    def sortString(self, s: str) -> str:
        # {char: count}
        counter = {}
        total_chars = len(s)

        for ch in s:
            if ch not in counter:
                counter[ch] = 0
            
            counter[ch] += 1
        
        sorted_keys = sorted(counter.keys())
        step = 1
        final_str = ""

        while total_chars > 0:
            if step == 1:
                for k in sorted_keys:
                    if counter[k] > 0:
                        final_str += k
                        counter[k] -= 1
                        total_chars -= 1
                step = 2
                continue
                    
            elif step == 2:
                for k in sorted_keys[::-1]:
                    if counter[k] > 0:
                        final_str += k
                        counter[k] -= 1
                        total_chars -= 1
                step = 1

        return final_str
    
obj = Solution()
final_str = obj.sortString("spo")
print(final_str)
