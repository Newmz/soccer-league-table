
import argparse
import os
import sys

def read_in_game_results(input_file):
    point_allocations = []
    game_results = open(input_file, 'r').readlines()
    for result in game_results:
        team1, team2 = _split_result_line(result)
        if team1[1] > team2[1]:
            team1_points_earned = 3
            team2_points_earned = 0
        elif team1[1] == team2[1]:
            team1_points_earned = 1
            team2_points_earned = 1
        else: 
            team1_points_earned = 0
            team2_points_earned = 3
        point_allocations.append([team1[0], team1_points_earned])
        point_allocations.append([team2[0], team2_points_earned])
    return point_allocations

def _split_result_line(result_string):
    team1, team2 = result_string.strip().split(", ")
    team1_name = "".join(team1[:-1]).strip()
    team2_name = "".join(team2[:-1]).strip()
    team1_score = int(team1[-1])
    team2_score = int(team2[-1])
    team1 = (team1_name, team1_score)
    team2 = (team2_name, team2_score)
    return team1, team2

def create_point_dict(point_allocations):
    point_dict = {}
    for pa in point_allocations:
        team = pa[0]
        points = pa[1]
        if team in point_dict:
            point_dict[team] += points
        else:
            point_dict[team] = points
    return point_dict

def output_league_table(point_dict):
    teams = sorted(point_dict.keys(), key=lambda x: point_dict[x], reverse=True)
    place = 0
    streak = 1
    prev_points = None
    for team in teams:
        points = point_dict[team]
        if prev_points != points:
            place += streak
            prev_points = points
            streak = 1
        else:
            streak += 1
        suffix = "pts" if points != 1 else "pt"
        print(f"{place}. {team}, {points} {suffix}")


if __name__ == "__main__":
    point_allocations = read_in_game_results("sample_input.txt")
    point_dict = create_point_dict(point_allocations)
    output_league_table(point_dict)



