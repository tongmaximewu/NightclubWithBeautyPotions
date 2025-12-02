# Bug:
#   - The time counter is incremented on every queue operation
#     (every time someone reaches the front), instead of only
#     when someone actually enters the club (beauty >= 8).
#
# This will produce a Wrong Answer on many test cases.

from collections import deque
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

    # queue holds (index, current_beauty, remaining_limit)
    q = deque((i, beauty[i], limit[i]) for i in range(n))

    time = 0  # INCORRECT: we will increment this every loop iteration

    while q:
        idx, b, lim = q.popleft()

        # WRONG: time increases even if nobody enters
        time += 1

        if b >= THRESHOLD:
            # person enters
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
        q.append((idx, b, lim))

    # queue empty, k never entered
    print(-1)


if __name__ == "__main__":
    main()
