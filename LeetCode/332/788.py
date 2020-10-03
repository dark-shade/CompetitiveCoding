"""152 ms
class Solution:
    def rotatedDigits(self, N: int) -> int:
        rot_same = {0,1,8}
        rot_swap = {2:5, 5:2, 6:9, 9:6}
        non_rot = {3,4,7}
        cnt = 0
        
        for n in range(1, N+1):
            n_rot = False
            curr = n
            new_num = 0
            place = 0
            
            while curr > 0:
                digit = curr % 10
                curr = int(curr/10)
                
                
                if digit in non_rot:
                    n_rot = True
                    break
                
                elif digit in rot_same:
                    new_num += digit * (10 ** place)
                    
                elif digit in rot_swap:
                    new_num += rot_swap[digit] * (10 ** place)
                    
                place += 1
                
            if not n_rot and new_num != n:
                print("n = ", n)
                print("new = ", new_num)
                cnt += 1
                
        return cnt
"""
"""164 ms
class Solution:
    def rotatedDigits(self, N: int) -> int:
        rot_same = {0,1,8}
        rot_swap = {2,5,6,9}
        non_rot = {3,4,7}
        
        cnt = 0
        
        for n in range(1, N+1):
            
            num_set = self.convertToSet(n)

            if len(num_set & non_rot) > 0:
                continue
                
            if len(rot_swap & num_set) == 0:
                continue
            else:
                cnt += 1
                
        return cnt
            
    def convertToSet(self, n):
        arr = set()
        
        while n > 0:
            arr.add(n%10)
            n = int(n/10)
            
        return arr
"""
"""100 ms
class Solution:
    def rotatedDigits(self, N: int) -> int:
        rot_same = {0,1,8}
        rot_swap = {2,5,6,9}
        non_rot = {3,4,7}
        cnt = 0
        
        for n in range(1, N+1):
            cnt_swap = 0
            cnt_non = 0
            while n > 0:
                curr = n % 10
                n = int(n/10)

                if curr in non_rot:
                    cnt_non += 1
                    break

                if curr in rot_swap:
                    cnt_swap += 1

            if cnt_swap > 0 and cnt_non == 0:
                cnt += 1
                
        return cnt
"""
