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
    if score >= score_levels[0]:
        return 1
    if score < score_levels[-1]:
        return len(score_levels) + 1
    low = 0
    high = len(score_levels) - 1
    while low < high:
        mid = (low + high) // 2
        if mid == low and score >= score_levels[high]:
            return high + 1
        if  score == score_levels[mid]:
            return mid + 1
        elif  score > score_levels[mid]:
            high = mid
        else:
            low = mid

if __name__ == '__main__':
    
    test_cases = ["test_cases/leaderboard_testcase07.txt", "test_cases/leaderboard_testcase03.txt"]
    answer_files = ["test_cases/leaderboard_output07.txt", "test_cases/leaderboard_output03.txt"]

    for test_case, answer_file in zip(test_cases, answer_files):
        fptr = open(test_case, 'r')
        scores_count = int(fptr.readline())
        scores = list(map(int, fptr.readline().rstrip().split()))
        alice_count = int(fptr.readline())
        alice = list(map(int, fptr.readline().rstrip().split()))
        fptr.close()
        answer = list(map(int, open(answer_file, "r").read().strip().split()))
        result = climbingLeaderboard(scores, alice)
        print(test_case, "preven true?", result == answer)

    
    # print(scores_count)
    # print(len(scores))
    # print(alice_count)
    # print(len(alice))
    # print(len(answer))
