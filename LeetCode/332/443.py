"""60 ms 14 MB
class Solution:
    def compress(self, chars: List[str]) -> int:
        insert_ptr = 0
        read_ptr = 0
        prev = ""
        cnt = 0
        final_len = 0
        
        while read_ptr < len(chars):
            if len(prev) == 0:
                prev = chars[read_ptr]
                cnt += 1
                read_ptr += 1
                continue
                
            if prev == chars[read_ptr]:
                cnt += 1
                read_ptr += 1
                
            elif prev != chars[read_ptr]:
                chars[insert_ptr] = prev
                insert_ptr += 1
                if cnt > 1:
                    if cnt < 10:
                        chars[insert_ptr] = str(cnt)
                        insert_ptr += 1
                        final_len += 2
                    else:
                        for ch in str(cnt):
                            chars[insert_ptr] = ch
                            insert_ptr += 1
                            final_len += 1
                        final_len += 1
                else:
                    final_len += 1
                cnt = 1
                prev = chars[read_ptr]
                read_ptr += 1
                
        chars[insert_ptr] = prev
        insert_ptr += 1
        if cnt > 1:
            if cnt < 10:                
                chars[insert_ptr] = str(cnt)
                final_len += 2
            else:
                for ch in str(cnt):
                    chars[insert_ptr] = ch
                    insert_ptr += 1
                    final_len += 1
                final_len += 1
        else:
            final_len += 1
                
        return final_len
"""
"""100 ms 13.9 MB
class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        
        while read < len(chars):
            cnt = 1
            for i in range(read + 1, len(chars)):
                if chars[i] == chars[read]:
                    cnt += 1
                else:
                    break
            
            chars[write] = chars[read]
            write += 1
            
            if cnt > 1:
                for ch in str(cnt):
                    chars[write] = ch
                    write += 1
                
            read += cnt
            
        return write
"""