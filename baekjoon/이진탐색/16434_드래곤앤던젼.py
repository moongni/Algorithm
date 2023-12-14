import sys

input = sys.stdin.readline

N, H_atack = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

# --------- 파라메트릭 서치 풀이 ----------
H_maxHP = 0
# 파라메트릭 서치 구간 설정
start = 0
end = sum([room[1] * (room[2] // H_atack) for room in rooms if room[0] == 1]) + 1
while start <= end:
    # 현재 공격력, 체력 초기화
    cur_atack = H_atack
    cur_hp = mid = (start + end) // 2
    is_clear = True
    # 클리어 할 수 있는지 확인
    for room in rooms:
        if room[0] == 1:
            cur_hp -= room[1] * (room[2] // cur_atack - (0 if room[2] % cur_atack else 1))
            if cur_hp <= 0:
                is_clear = False
                break
        else:
            cur_atack += room[1]
            cur_hp = min(mid, cur_hp + room[2])

    # 서치 구간 재설정
    if not is_clear:
        start = mid + 1
    else:
        H_maxHP = mid
        end = mid - 1
    
print(H_maxHP)


# --------- DP라고 볼 수도 있을 듯한 풀이 ----------
cur_atack = H_atack
max_damages = 0
damages = 0
for room in rooms:
    if room[0] == 1:
        damages += room[1] * (room[2] // cur_atack - (0 if room[2] % cur_atack else 1))
        max_damages = max(max_damages, damages)
    else:
        cur_atack += room[1]
        damages = max(0, damages - room[2])
        
print(max_damages + 1)