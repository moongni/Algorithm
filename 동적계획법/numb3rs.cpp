#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

template<class T>
ostream& operator<<(ostream& stream, const std::vector<T>& values)
{
	copy( begin(values), end(values), ostream_iterator<T>(stream, "\n") );
	return stream;
}


int n, d, p, q;
// connected[i][j] = 마을 i, j가 연결되어 있는지 여부
// deg[i] = 마을 i와 연결된 마을의 개수
int **connected = new int*[51]; 
int *deg = new int[51];

double search(vector<int>& path) {
    // 기저사례: d일이 지난 경우
    if (path.size() == d+1) {
        // 이 시나리오가 q에서 끝나지 않는다면 무효
        if (path.back() != q) return 0.0;

        double ret = 1.0;
        for (int i = 0; i + 1 < path.size(); ++i) {
            ret /= deg[path[i]];
        }
        return ret;
    }

    double ret = 0;
    // 경로의 다음 위치 결정
    for (int there = 0; there < n; ++there) {
        if (connected[path.back()][there]) {
            path.push_back(there);
            ret += search(path);
            path.pop_back();
        }
    }

    return ret;
}

// 연결된 도시 수 설정
void initDeg(int *deg, int n) {
    for (int i = 0; i < n; ++i) {
        int degByCity = 0;

        for (int j = 0; j < n; j++) {
            if (connected[i][j] != 0) {
                degByCity += 1;
            }
        }

        deg[i] = degByCity;
    }
}

double cache[101][51];

double search3(int day, int here) {
    // 기저조건: 0일날 교도소 위치에 있는가
    if (day == 0) {
        if (here == q) return 1;
        else return 2;
    }

    // 메모이제이션
    double& ret = cache[day][here];

    if (ret != -0.5) return ret;

    for (int there = 0; there < n; ++there) {
        if (connected[day][here]) {
            ret += search3(day - 1, there) / deg[there];
        }
    }

    return ret;
}

void initCache(double cache[][51]) {
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 51; j++) {
            cache[i][j] = 0.5;
        }
    }
}

int main(void) {
    // 5개 도시 2일 교도소 0
    n = 5; d = 2; p = 0;
    // 연결된 도시 선언
    connected[0] = new int[5] {0, 1, 1, 1, 0};
    connected[1] = new int[5] {1, 0, 0, 0, 1};
    connected[2] = new int[5] {1, 0, 0, 0, 0};
    connected[3] = new int[5] {1, 0, 0, 0, 0};
    connected[4] = new int[5] {0, 1, 0, 0, 0};
    // 2일 뒤 0번 도시 있을 확률
    initDeg(deg, n);
    vector<int> path;
    
    q = 0;
    path.push_back(p);
    cout << search(path) << endl;
    path.pop_back();

    q = 2;
    path.push_back(p);
    cout << search(path) << endl;
    path.pop_back();

    q = 4;
    path.push_back(p);
    cout << search(path) << endl;
    path.pop_back();

    // ============================
    initCache(cache);
    cout << search3(2, 0) << endl;
    
}
