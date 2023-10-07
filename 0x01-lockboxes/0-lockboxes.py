#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes
"""


def find(parent, i):
    """Return True if all boxes can be opened, else return False"""
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def canUnlockAll(boxes):
    n = len(boxes)
    parent = list(range(n))
    rank = [0] * n

    for i in range(n):
        for key in boxes[i]:
            if key < n:
                union(parent, rank, i, key)

    for i in range(1, n):
        if find(parent, i) != find(parent, 0):
            return False

    return True
