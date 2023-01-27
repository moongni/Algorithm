#include <iostream>

using namespace std;

const int MOD = 10 * 1000 * 1000;
int cache[101][101];

void initCache(int cache[][101]) {
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j ++) {
            cache[i][j] = -1;
        }
    }
}

void printCache(int cache[][101]) {
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            cout << cache[i][j];            
        }
        cout << endl;
    }
}

int poly(int n, int first=0) {
    // 기저조건 n == first
    if (n == first) return 1;
    // 메모이제이션
    int& ret = cache[n][first];

    if (ret != -1) return ret;

    ret = 0;

    for (int second = 1; second <= n-first; ++second) {
        int add = second + first - 1;
        add *= poly(n - first, second);
        add %= MOD;
        ret += add;
        ret %= MOD;
    }

    return ret;
}

int solve(int n) {
    initCache(cache);

    int ret = 0;

    for(int i = 1; i <= n; i++) {
        ret += poly(n, i);
    }

    return ret;
}

int main(void) {
    cout << solve(2) << endl;
    cout << solve(4) << endl;
    cout << solve(92) << endl;
}