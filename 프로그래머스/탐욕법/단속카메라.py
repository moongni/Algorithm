def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    camera = routes[0][1]
    print(routes)
    print(camera)
    for i in range(1, len(routes)):
        if routes[i][0] <= camera:
            if camera > routes[i][1]:
                print("include", routes[i])
                print(camera)
                camera = routes[i][1]
            continue
        print("cut")
        print(camera)
        camera = routes[i][1]
        print(camera)
        answer += 1
        
    return answer + 1

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))