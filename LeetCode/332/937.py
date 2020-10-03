"""68 ms 13.9 MB
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) == 0:
            return []
        
        sorted_logs = []
        num_logs = []
        
        # of form {msg: identifier}
        log_dict = {}
        
        for log in logs:
            if log[len(log) - 1].isalpha():
                iden, msg = self.getIden(log)
                
                if msg not in log_dict:
                    log_dict[msg] = []
                
                log_dict[msg].append(iden)
            else:
                num_logs.append(log)
            
        for msg in sorted(list(log_dict.keys())):
            for iden in sorted(log_dict[msg]):
                sorted_logs.append(iden + " " + msg)

        sorted_logs.extend(num_logs)

        return sorted_logs
                
                
    def getIden(self, log: str) -> (str, str):
        for i in range(len(log)):
            if log[i] == " ":
                break
                
        return (log[:i], log[i+1:])
"""
"""48 ms 13.9 MB
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        numbers = []
        
        for log in logs:
            if log.split()[1].isdigit():
                numbers.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split()[0])
        letters.sort(key=lambda x: x.split()[1:])
            
        letters.extend(numbers)
        
        return letters
"""