#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    keys = [0]  # Start with the key for box 0

    while keys:
        current_box = keys.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                keys.append(key)

    return all(visited)
