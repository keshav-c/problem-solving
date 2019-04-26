# Climbing the Leaderboard

Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses [Dense Ranking](https://en.wikipedia.org/wiki/Ranking#Dense_ranking_.28.221223.22_ranking.29), so its leaderboard works like this:

The player with the highest score is ranked number **1** on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
For example, the four players on the leaderboard have high scores of **100**, **90**, **90**, and **80**. Those players will have ranks **1**, **2**, **2**, and **3**, respectively. If Alice's scores are **70**, **80** and **105**, her rankings after each game are **4<sup>th</sup>**, **3<sup>rd</sup>** and **1<sup>st</sup>**.

## Function Description

Complete the `climbingLeaderboard` function. It should return an integer array where each element represents Alice's rank after the game.

`climbingLeaderboard` has the following parameter(s):

- `scores`: an array of integers that represent leaderboard scores
- `alice`: an array of integers that represent Alice's scores

Hackerrank link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

I initially solved this using brute force which is easier to code for, but many test cases timed out.

Since the `scores` array is already sorted in descending order, binary search is ideal. Slight difference is that search *has* to return a positional match rather than just an exact element match. `get_rank` function, that I wrote, does this and even skips searching at the end points.