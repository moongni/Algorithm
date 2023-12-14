def solution(genres, plays):
    plays_by_genres = {}
    plays_by_id = {}

    for i in range(len(genres)):
        if plays_by_genres.get(genres[i]):
            plays_by_genres[genres[i]] += plays[i]
            plays_by_id[genres[i]].append([i, plays[i]])
        else:
            plays_by_genres[genres[i]] = plays[i]
            plays_by_id[genres[i]]= [[i, plays[i]]]

    answer = []

    for genre in sorted([[key, value] for key, value in plays_by_genres.items()], key=lambda x: x[1], reverse=True):
        most_played = sorted(plays_by_id[genre[0]], key=lambda x: x[1], reverse=True)

        for i in range(min(2, len(most_played))):
            answer.append(most_played[i][0])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))