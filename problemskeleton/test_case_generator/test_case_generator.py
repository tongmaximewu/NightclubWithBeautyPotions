import random
import sys

def solve():
    # Usage: python3 generator.py [mode] [args...]
    #
    # MODES:
    #   sample:         The PDF sample case
    #   random N L:     Standard random case (Size N, Max Limit L)
    #   stress N:       Max processing (Beauty 1, High Limits) -> TLE test
    #   edge_min:       N=1 case
    #   edge_kicked N:  Everyone (including K) runs out of potions
    #   mixed_chaos N:  Mix of people entering immediately, cycling, and failing
    
    if len(sys.argv) < 2:
        print("Usage: generator.py [mode] [args]", file=sys.stderr)
        sys.exit(1)

    mode = sys.argv[1]

    # 1. Sample Case 
    if mode == "sample":
        print("3")
        print("7 5 8")
        print("2 2 0")
        print("1")
        return

    # 2. Standard Random 
    if mode == "random":
        n = int(sys.argv[2])
        max_limit = int(sys.argv[3])
        
        beauty = [random.randint(1, 10) for _ in range(n)]
        limit = [random.randint(0, max_limit) for _ in range(n)]
        k = random.randint(0, n - 1)
        
        print(n)
        print(*(beauty))
        print(*(limit))
        print(k)
        return

    # 3. Stress Test 
    # Everyone starts at Beauty 1 and has plenty of potions.
    # They all must cycle 7 times to reach Beauty 8.
    # This forces the simulation to run the maximum number of steps.
    if mode == "stress":
        n = int(sys.argv[2])
        beauty = [1] * n
        limit = [100] * n  # Plenty of potions to reach 8
        k = n - 1          # We track the last person to ensure full simulation
        
        print(n)
        print(*(beauty))
        print(*(limit))
        print(k)
        return

    # 4. Edge Case: Minimum Size
    if mode == "edge_min":
        n = 1
        beauty = [random.randint(1, 9)] # Either enters or cycles
        limit = [random.randint(0, 5)]
        k = 0
        
        print(n)
        print(*(beauty))
        print(*(limit))
        print(k)
        return

    # 5. Edge Case: All Kicked
    # Everyone needs potions but has 0 (or not enough).
    # This tests if the code correctly handles "leaving queue without entering".
    if mode == "edge_kicked":
        n = int(sys.argv[2])
        beauty = [1] * n        # Far from 8
        limit = [2] * n         # Not enough potions (need 7)
        k = random.randint(0, n - 1)
        
        print(n)
        print(*(beauty))
        print(*(limit))
        print(k)
        return

    # 6. Complicated Random
    # Intentionally mixes people who enter instantly (8+), 
    # people who barely make it (7, limit 1), 
    # and people who fail (7, limit 0).
    if mode == "mixed_chaos":
        n = int(sys.argv[2])
        beauty = []
        limit = []
        
        for _ in range(n):
            r = random.random()
            if r < 0.33:
                # Group A: Enters immediately
                beauty.append(random.randint(8, 10))
                limit.append(0)
            elif r < 0.66:
                # Group B: Needs potions, has enough
                b = random.randint(1, 7)
                needed = 8 - b
                beauty.append(b)
                limit.append(needed + random.randint(0, 2))
            else:
                # Group C: Needs potions, fails
                b = random.randint(1, 7)
                needed = 8 - b
                beauty.append(b)
                limit.append(needed - 1) # Just barely fails
                
        k = random.randint(0, n - 1)
        
        print(n)
        print(*(beauty))
        print(*(limit))
        print(k)
        return

if __name__ == "__main__":
    solve()