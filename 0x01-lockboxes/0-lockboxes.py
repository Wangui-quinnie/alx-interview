#!/usr/bin/python3
"""
Methid that determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list of list): A list of lists representing the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
