def solution(array, commands):
    answer = []
    for command in commands:
        temp_arr = array[command[0] - 1: command[1]]
        temp_arr.sort()
        answer.append(temp_arr[command[2] - 1])
    return answer