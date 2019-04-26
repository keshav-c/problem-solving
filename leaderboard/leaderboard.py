#!/bin/python3

def climbingLeaderboard(scores, alice):
    score_levels = [scores[0]]
    for score in scores[1:]:
        if score != score_levels[-1]:
            score_levels.append(score)
    alice_ranks = []
    for a_score in alice:
        alice_ranks.append(get_rank(score_levels, a_score))
    return alice_ranks

def get_rank(score_levels, score):
    if score > score_levels[0]:
        return 1
    if score < score_levels[-1]:
        return len(score_levels) + 1
    low = 0
    high = len(score_levels) - 1
    while low < high:
        mid = (low + high) // 2
        if mid == low:
            if score >= score_levels[high]:
                return high + 1
        if  score == score_levels[mid]:
            return mid + 1
        elif  score > score_levels[mid]:
            high = mid
        else:
            low = mid
    if score > score_levels[mid]:
        return mid + 1
    if score < score_levels[mid]:
        return mid + 2


if __name__ == '__main__':
    fptr = open("leaderboard_testcase07.txt", 'r')
    scores_count = int(fptr.readline())
    scores = list(map(int, fptr.readline().rstrip().split()))
    alice_count = int(fptr.readline())
    alice = list(map(int, fptr.readline().rstrip().split()))
    fptr.close()
    
    answer = list(map(int, open("leaderboard_output07.txt", "r").read().strip().split()))

    result = climbingLeaderboard(scores, alice)
    
    print(result == answer)

    
    # print(len(answer))
    # print(scores_count)
    # print(len(scores))
    # print(alice_count)
    # print(len(alice))

    
