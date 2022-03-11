import pytest
from LeagueTable import LeagueTable, Team

class TestEnv():
    def __init__(self):
        self.table = LeagueTable()
        self.sample_output = open("test_outputs/expected-output.txt").read()
        self.empty_output = open("test_outputs/empty_output.txt").read()



class TestLeagueTable_BlackBox():
    def test_sample_io(self):
        te = TestEnv()
        te.table.read_in_game_results("test_inputs/sample-input.txt")
        assert te.sample_output == te.table.__str__()
    
    def test_empty_file(self):
        te = TestEnv()
        te.table.read_in_game_results("test_inputs/empty_input.txt")
        assert te.empty_output == te.table.__str__()

class TestLeagueTable_Internals():
    def test_clear(self):
        te = TestEnv()
        te.table.read_in_game_results("test_inputs/sample-input.txt")
        te.table.clear_table()
        assert te.empty_output == te.table.__str__()
