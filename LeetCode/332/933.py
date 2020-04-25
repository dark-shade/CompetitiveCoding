"""
class RecentCounter:

    def __init__(self):
        self.pingTimes = []  

    def ping(self, t: int) -> int:
        self.pingTimes.append(t)
        new_list = []

        cnt = 0

        for pingTime in self.pingTimes:
            if pingTime < t - 3000:
                continue
            new_list.append(pingTime)
            cnt += 1
        
        self.pingTimes = new_list

        return cnt
"""
class RecentCounter:
    def __init__(self):
        self.pingTimes = []

    def ping(self, t: int) -> int:
        self.pingTimes.append(t)
    
        for i, pingTime in enumerate(self.pingTimes[::-1]):
            if pingTime < t - 3000:
                return len(self.pingTimes[len(self.pingTimes) - i - 1:])
            
        return len(self.pingTimes)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)