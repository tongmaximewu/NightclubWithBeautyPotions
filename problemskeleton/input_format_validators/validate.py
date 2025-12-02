import sys
import re

def main():
    # 1. Validate first line: N only
    line = sys.stdin.readline()
    if not re.match(r'^[1-9][0-9]*\n$', line):
        sys.exit(43)
    n = int(line.strip())
    
    # Global constraints
    if not (1 <= n <= 100000):
        sys.exit(43)

    # Validate second line: Beauty Scores
    line = sys.stdin.readline()
    if not re.match(r'^[1-9][0-9]*( [1-9][0-9]*)*\n$', line):
        sys.exit(43)
    beauty = list(map(int, line.split()))
    if len(beauty) != n:
        sys.exit(43)
    for b in beauty:
        if not (1 <= b <= 10):
            sys.exit(43)

    # Validate third line: Potion limits
    line = sys.stdin.readline()
    # Allow 0, no leading zeros otherwise
    if not re.match(r'^(0|[1-9][0-9]*)( (0|[1-9][0-9]*))*\n$', line):
        sys.exit(43)
    limits = list(map(int, line.split()))
    if len(limits) != n:
        sys.exit(43)
    for l in limits:
        if not (0 <= l <= 100):
            sys.exit(43)

    # Validate fourth line: K only
    line = sys.stdin.readline()
    # 0 or positive integer
    if not re.match(r'^(0|[1-9][0-9]*)\n$', line):
        sys.exit(43)
    k = int(line.strip())
    
    if not (0 <= k < n):
        sys.exit(43)

    # Ensure no extra input
    if sys.stdin.readline() != '':
        sys.exit(43)

    # on success
    sys.exit(42)

if __name__ == "__main__":
    main()