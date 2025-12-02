from collections import deque
import sys

"""
Nightclub Queue with Beauty Potions

Input:
    n
    beauty[0..n-1]
    limit[0..n-1]
    k

Output:
    The time (number of people admitted before and including k)
    at which person k enters the club, or -1 if they never enter.

Algorithm:
    Use a queue of (idx, beauty, limitRemaining).
    Process the front person according to the rules:
        - If beauty >= 8: they enter; time += 1.
          If idx == k: print time and exit.
        - Else if limit == 0: kicked out.
          If idx == k: print -1 and exit.
        - Else: beauty++, limit--, push back to queue (no time added).
    Because each person can increase their beauty at most up to 8
    before entering (or run out of limit), each person appears at
    the front of the queue O(1) times, so total time is O(n).
"""

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

    q = deque((i, beauty[i], limit[i]) for i in range(n))

    time = 0  # how many people have entered so far

    while q:
        idx, b, lim = q.popleft()

        if b >= THRESHOLD:
            time += 1
            if idx == k:
                print(time)
                return
            # person leaves the system
            continue

        if lim == 0:
            if idx == k:
                print(-1)
                return
            # kicked out permanently
            continue

        # give one potion and move to the back (instant, no time)
        b = min(b + 1, MAX_BEAUTY)
        lim -= 1
        q.append((idx, b, lim))

    # queue empty and k never entered
    print(-1)


if __name__ == "__main__":
    main()
