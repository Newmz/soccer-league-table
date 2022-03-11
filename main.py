
import argparse
import os
import sys

from LeagueTable import LeagueTable, Team


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file", help="Text file containing one game result per line")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    table = LeagueTable()
    point_allocations = table.read_in_game_results(args.input_file)
    print(table)



