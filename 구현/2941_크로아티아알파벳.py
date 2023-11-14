import sys

input = sys.stdin.readline
string = input().rstrip()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

def solution(string):
    for c in croatia:
        string = string.replace(c, "1")
    return len(string)

print(solution(string))