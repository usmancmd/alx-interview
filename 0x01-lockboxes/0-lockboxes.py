#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""

    n = len(boxes)
    unlocked_boxes = set()
    keys_to_check = set()

    unlocked_boxes.add(0)
    keys_to_check.update(boxes[0])

    while keys_to_check:
        key = keys_to_check.pop()
        if key < 0 or key >= n:
            continue

        if key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys_to_check.update(boxes[key])

    return len(unlocked_boxes) == n
