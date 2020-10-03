from typing import List

"""
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # of form {"R/p/B" : [[xi, yi]]}
        locations = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    if "R" not in locations:
                        locations["R"] = []
                    locations["R"].append([i,j])

                elif board[i][j] == "p":
                    if "p" not in locations:
                        locations["p"] = []
                    locations["p"].append([i,j])

                if board[i][j] == "B":
                    if "B" not in locations:
                        locations["B"] = []
                    locations["B"].append([i,j])

        cnt = 0

        if "p" in locations:
            for xp, yp in locations["p"]:
                if xp == locations["R"][0][0] or yp == locations["R"][0][1]:
                    cnt += 1

        return cnt
"""
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        y_R = -1
        x_R = -1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    x_R = i
                    y_R = j
                    break
                    
        cnt = 0

        # North
        for i in range(1, x_R + 1):
            if board[x_R - i][y_R] == "p":
                cnt += 1
                break

            if board[x_R - i][y_R] == "B":
                break
        
        # South
        for i in range(x_R + 1, len(board)):
            if board[i][y_R] == "p":
                cnt += 1
                break

            if board[i][y_R] == "B":
                break

        # East
        for j in range(1, y_R + 1):
            if board[x_R][y_R - j] == "p":
                cnt += 1
                break

            if board[x_R][y_R - j] == "B":
                break

        # West
        for j in range(y_R + 1, len(board[0])):
            if board[x_R][j] == "p":
                cnt += 1
                break

            if board[x_R][j] == "B":
                break

        return cnt
