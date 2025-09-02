from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            Ax, Ay = points[i]
            for j in range(n):
                if i == j:
                    continue
                Bx, By = points[j]

                if Ax <= Bx and Ay >= By and (Ax < Bx or Ay > By):
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        Cx, Cy = points[k]
                        if Ax <= Cx <= Bx and By <= Cy <= Ay:
                            valid = False
                            break

                    if valid:
                        count += 1
        return count
