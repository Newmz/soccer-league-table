import pytest
from LeagueTable import LeagueTable, Team

"""
Unfortunately I am doing this on a windows system and had to spend about 15 minutes setting up pytest env
"""

class TestEnv():
    def __init__(self):
        self.table = LeagueTable()
        self.sample_output = open("test_outputs/sample_output.txt").read()



class TestLeaugeTable():
    def test_sample_io(self):
        te = TestEnv()
        te.table.read_in_game_results("test_inputs/sample_input.txt")
        assert te.sample_output == te.table.__str__()