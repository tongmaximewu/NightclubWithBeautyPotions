# Correct logic, but intentionally inefficient queue usage.
#
# We implement the queue as a Python list and use pop(0),
# which is O(n) each time (because it shifts all remaining elements).
#
# Overall complexity becomes roughly O(n^2), which is prone to
# TLE on large test cases.

import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))

    beauty = [int(next(it)) for _ in range(n)]
    limit = [int(next(it)) for _ in range(n)]
    k = int(next(it))

    THRESHOLD = 8
    MAX_BEAUTY = 10

    # queue will store indices
    queue = list(range(n))
    cur_beauty = beauty[:]
    cur_limit = limit[:]

    time = 0  # counts how many people have entered

    while queue:
        # inefficient: pop(0) is O(len(queue)), causing O(n^2) behavior
        idx = queue.pop(0)
        b = cur_beauty[idx]
        lim = cur_limit[idx]

        if b >= THRESHOLD:
            time += 1
            if idx == k:
                print(time)
                return
            # they leave the system
            continue

        if lim == 0:
            # kicked out
            if idx == k:
                print(-1)
                return
            continue

        # give potion and move to back
        b = min(b + 1, MAX_BEAUTY)
        lim -= 1
        cur_beauty[idx] = b
        cur_limit[idx] = lim
        queue.append(idx)

    # queue empty, k never entered
    print(-1)


if __name__ == "__main__":
    main()
