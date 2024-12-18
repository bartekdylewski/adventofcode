import os
import sys
from collections import defaultdict, Counter, deque
import math
import numpy as np
import scipy
import pprint
import heapq
sys.setrecursionlimit(10 ** 9)

# N E S W
DIR_MAP = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIR_SZ = len(DIR_MAP)

def printGrid(grid):

    for line in grid:
        print(''.join(line))


def solve1(grid, startPos, endPos):
    # i, j = robotPos[0], robotPos[1]
    m, n = len(grid), len(grid[0])

    dist = []

    for _ in range(m):
        dist.append([[float('inf')] * DIR_SZ for _ in range(n)])

    # print(dist)
    pq = []
    heapq.heappush(pq, (0, startPos[0], startPos[1], 1))

    # qu.append((startPos[0], startPos[1], 1))
    dist[startPos[0]][startPos[1]][1] = 0
    dist[startPos[0]][startPos[1]][0] = 0
    dist[startPos[0]][startPos[1]][2] = 0
    dist[startPos[0]][startPos[1]][3] = 0

    while pq:
        # print(pq)
        coord = heapq.heappop(pq)

        score, i, j, dirInd = coord

        if (i, j) == endPos:
            continue

        negDir = (dirInd + 2) % DIR_SZ

        for ind, dir in enumerate(DIR_MAP):
            if ind == negDir:
                continue

            x, y = i + dir[0], j + dir[1]
            newScore = 1001

            if dirInd == ind:
                newScore = 1

            if 0 <= x < m and 0 <= y < n and grid[x][y] != "#" and dist[x][y][ind] > dist[i][j][dirInd] + newScore:
                dist[x][y][ind] = score + newScore
                heapq.heappush(pq, (dist[x][y][ind], x, y, ind))
    
    print("Soln 1:" , min(dist[endPos[0]][endPos[1]]))

def backTrack(tiles: set, grid, endPos, dist, i, j, dirInd):
    # print(i, j, endPos)

    score = dist[i][j][dirInd]

    tiles.add((i, j))

    if (i, j) == endPos:
        return

    for dir in DIR_MAP:
        # if dirInd == ind:
        #     continue
        
        x, y = i + dir[0], j + dir[1]

        for ind, oldScore in enumerate(dist[x][y]):
            if oldScore == score - 1 or oldScore == score - 1001:
                backTrack(tiles, grid, endPos, dist, x, y, ind)

    return 0

def solve2(grid, startPos, endPos):
    # backtrack mf
    # i, j = robotPos[0], robotPos[1]
    m, n = len(grid), len(grid[0])

    dist = []

    for _ in range(m):
        dist.append([[float('inf')] * DIR_SZ for _ in range(n)])

    # print(dist)
    pq = []
    heapq.heappush(pq, (0, startPos[0], startPos[1], 1))

    # qu.append((startPos[0], startPos[1], 1))
    dist[startPos[0]][startPos[1]][1] = 0
    dist[startPos[0]][startPos[1]][0] = 0
    dist[startPos[0]][startPos[1]][2] = 0
    dist[startPos[0]][startPos[1]][3] = 0

    while pq:
        # print(pq)
        coord = heapq.heappop(pq)

        score, i, j, dirInd = coord

        if (i, j) == endPos:
            continue

        negDir = (dirInd + 2) % DIR_SZ

        for ind, dir in enumerate(DIR_MAP):
            if ind == negDir:
                continue

            x, y = i + dir[0], j + dir[1]
            newScore = 1001

            if dirInd == ind:
                newScore = 1

            if 0 <= x < m and 0 <= y < n and grid[x][y] != "#" and dist[x][y][ind] > dist[i][j][dirInd] + newScore:
                # if dist[x][y] < newScore:
                dist[x][y][ind] = score + newScore
                heapq.heappush(pq, (dist[x][y][ind], x, y, ind))
    
    i, j = endPos
    # backtrack score and paths that go to that score

    # while i != startPos[0] and j != startPos[1]:
    tiles = set()

    di, md = -1, float('inf')
    for ind, score in enumerate(dist[i][j]):
        if score < md:
            md = score
            di = ind


    backTrack(tiles, grid, startPos, dist, endPos[0], endPos[1], di)
    print("Tiles: ", len(tiles))

    print("Soln 2:" , min(dist[endPos[0]][endPos[1]]))


startPos, endPos = None, None
with open("iinput/input16.txt", "r") as f:
    grid = []
    i = 0

    for line in f.readlines():
        grid.append(list(line.strip()))

        for j in range(len(line)):
            if line[j] == "S":
                startPos = (i, j)
                break
            elif line[j] == "E":
                endPos = (i, j)
                break
        i += 1
    # grid = [listi.strip() for i in f.readlines()]

# printGrid(grid)
print(f"Start : {startPos}, End : {endPos}, Dir: {DIR_MAP[1]}")

solve1(grid, startPos, endPos)
solve2(grid, startPos, endPos)
