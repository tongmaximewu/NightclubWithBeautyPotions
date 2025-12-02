# This code crashes with ZeroDivisionError when handling specific edge cases.

from collections import deque
import sys

def main():
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

    q = deque((i, beauty[i], limit[i]) for i in range(n))

    time = 0

    while q:
        idx, b, lim = q.popleft()

        if b >= THRESHOLD:
            time += 1
            if idx == k:
                print(time)
                return
            continue

        # BUG: Calculating "potions needed" causes division by 0 if limit is 0.
        # This crashes specifically on cases where people get kicked out.
        turns_needed = (THRESHOLD - b) / lim 

        if lim == 0:
            if idx == k:
                print(-1)
                return
            continue

        b = min(b + 1, MAX_BEAUTY)
        lim -= 1
        q.append((idx, b, lim))

    print(-1)

if __name__ == "__main__":
    main()