""" 32 ms
class Solution:        
    def dayOfTheWeek(self, d, m, y):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[datetime.datetime(y, m, d).weekday()]
"""