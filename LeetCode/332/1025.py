"""
# TLE
class Solution:
    def divisorGame(self, N: int) -> bool:
        r = self.getWinner(N, "A")
        if r == 0:
            return False
        
        return True
        
        
    def getWinner(self, N, turn):
        # base condition
        if N == 1:
            if turn == "A":               
                return 0
            else:
                return 1

        # get divisors
        divisors = [1]
        for n in range(2, N):
            if N % n == 0:
                if n == divisors[-1]:
                    break
                divisors.append(n)
                divisors.append(int(N/n))

        next_turn = ""
        if turn == "A":
            next_turn = "B"
        else:
            next_turn = "A"        
    
        results = []

        for d in divisors:
            results.append(self.getWinner(N - d, next_turn))

        return max(results)
"""
class Solution:
    def divisorGame(self, N: int) -> bool:
        turn = "A"

        while N > 1:
            if N % 2 == 0:
                n = self.getMaxDiv(N, "O")
                N -= n
            else:
                n = self.getMaxDiv(N, "E")
                N -= n

            if turn == "A":
                turn = "B"
            else:
                turn = "A"
        
        if turn == "A":
            return False

        return True
                

    def getMaxDiv(self, N, EO):
        # get divisors
        divisors = [1]
        for n in range(2, N):
            if N % n == 0:
                if n == divisors[-1]:
                    break
                divisors.append(n)
                divisors.append(int(N/n))
        
        for n in divisors[::-1]:
            if (n % 2 == 0 and EO == "E") or (n % 2 != 0 and EO == "O"):
                return n

        return 1            

