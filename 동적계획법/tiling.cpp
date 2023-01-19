#include <iostream>
#define MAX_WIDTH 101

using namespace std;

const int MOD = 1000000007;

int cache[MAX_WIDTH];

void initialzeCache(int *cache, int value) {
    for (int i = 0; i < sizeof(cache); i++) {
        cache[i] = value;
    }        
}

int tiling(int width) {
    if ( width <= 1 ) return 1;

    int& ret = cache[width];

    if (ret != -1) return ret;

    return ret = (tiling(width - 1) + tiling(width - 2)) % MOD;
}

int helptiling(int width) {
    initialzeCache(cache, -1);

    return tiling(width);
}

int asyntiling(int width) {
    // 홀수일 경우
    if ( width % 2 == 1 ) 
        return (helptiling(width) - helptiling(width / 2) + MOD) % MOD;

    // 짝수의 경우
    int ret = helptiling(width);
    ret = (ret - helptiling(width / 2) + MOD) % MOD;
    ret = (ret - helptiling(width / 2 - 1) + MOD) % MOD;
    return ret;    
}

int cache2[MAX_WIDTH];

int asyntiling2(int width) {
    if (width <= 2) return 0;

    int& ret = cache2[width];
    
    if (ret != -1) return ret;

    ret = asyntiling2(width - 2) % MOD;
    ret = (ret + asyntiling2(width - 4)) % MOD;
    ret = (ret + helptiling(width - 3)) % MOD;
    ret = (ret + tiling(width  -3)) % MOD;

    return ret;
}

int main(void) {
    initialzeCache(cache2, -1);
    cout << asyntiling2(2) << endl;
    initialzeCache(cache2, -1);
    cout << asyntiling2(4) << endl;
    initialzeCache(cache2, -1);
    cout << asyntiling2(92) << endl;
}
