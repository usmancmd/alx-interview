#!/usr/bin/env python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    all_box_length = len(boxes)

    unlocked_boxes = set()
    checked_keys = set()

    unlocked_boxes.add(0)
    checked_keys.update(boxes[0])

    while checked_keys:
        key = checked_keys.pop()
        if key < 0 or key >= all_box_length:
            continue

        if key not in unlocked_boxes:
            unlocked_boxes.add(key)
            checked_keys.update(boxes[key])

    final_answer = len(unlocked_boxes) == all_box_length
    return final_answer
