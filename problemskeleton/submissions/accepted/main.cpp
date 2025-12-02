#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

/*
 * Nightclub Queue with Beauty Potions
 *
 * We simulate the queue using a FIFO structure (std::queue).
 * Each person i is represented as a struct with:
 *   - idx  : original index in [0, n-1]
 *   - b    : current beauty score
 *   - lim  : remaining number of potions they may drink
 *
 * Rules at each step:
 *   1. Take the person at the front.
 *   2. If b >= 8:
 *        - they enter; time++.
 *        - if idx == k, return time.
 *   3. Else (b < 8):
 *        - if lim == 0:
 *             - they are kicked out; if idx == k, return -1.
 *        - else:
 *             - give one potion: b = min(b + 1, 10), lim--,
 *               push them to the back.
 *
 * Important observation:
 *   A person needs at most max(0, 8 - starting_beauty) potions
 *   and then one final step to enter. Since starting_beauty >= 1
 *   and threshold is 8, this is at most 7 + 1 = 8 queue visits.
 *   So total operations are O(n), which is efficient.
 */

struct Person {
    int idx;
    int beauty;
    int limit;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) {
        return 0; // no input
    }

    vector<int> beauty(n), limitArr(n);
    for (int i = 0; i < n; ++i) cin >> beauty[i];
    for (int i = 0; i < n; ++i) cin >> limitArr[i];

    int k;
    cin >> k;

    const int THRESHOLD = 8;
    const int MAX_BEAUTY = 10;

    queue<Person> q;
    for (int i = 0; i < n; ++i) {
        Person p = {i, beauty[i], limitArr[i]};
        q.push(p);
    }

    long long time = 0;  // number of people who have entered so far

    while (!q.empty()) {
        Person p = q.front();
        q.pop();

        // Person is already beautiful enough to enter
        if (p.beauty >= THRESHOLD) {
            ++time;
            if (p.idx == k) {
                cout << time << "\n";
                return 0;
            }
            // they leave the system
            continue;
        }

        // Not enough beauty, and no potions left -> kicked out
        if (p.limit == 0) {
            if (p.idx == k) {
                cout << -1 << "\n";
                return 0;
            }
            continue;
        }

        // Not enough beauty, but can drink a potion
        p.beauty = min(p.beauty + 1, MAX_BEAUTY);
        --p.limit;
        q.push(p);
    }

    // Queue emptied, target never entered
    cout << -1 << "\n";
    return 0;
}
