class LeagueTable:
    def __init__(self):
        self.teams = []
    
    def __str__(self):
        output_str = ""
        self.teams = sorted(self.teams, reverse=True)
        place = 0
        streak = 1
        prev_points = None
        for team in self.teams:
            if prev_points != team.points:
                place += streak
                prev_points = team.points
                streak = 1
            else:
                streak += 1
            suffix = "pts" if team.points != 1 else "pt"
            output_str += f"{place}. {team.name}, {team.points} {suffix}\n"
        return output_str  # or output_str[:-1] - couldn't tell if I placed newline into output when moving files

    def read_in_game_results(self, input_file):
        game_results = open(input_file, 'r').readlines()
        for result in game_results:
            team1, team2 = self._split_result_line(result)
            if team1[1] > team2[1]:
                team1_points_earned = 3
                team2_points_earned = 0
            elif team1[1] == team2[1]:
                team1_points_earned = 1
                team2_points_earned = 1
            else: 
                team1_points_earned = 0
                team2_points_earned = 3
            self._add_game_result({"name": team1[0], "points": team1_points_earned})
            self._add_game_result({"name": team2[0], "points": team2_points_earned})
    
    def clear_table(self):
        self.teams = []

    def _add_game_result(self, result):
        for team in self.teams:
            if team.name == result["name"]:
                team.add_points(result["points"])
                return
        self.teams.append(Team(result["name"]))
        self.teams[-1].add_points(result["points"])

    def _split_result_line(self, result_string):
        team1, team2 = result_string.strip().split(", ")
        team1_name = "".join(team1[:-1]).strip()
        team2_name = "".join(team2[:-1]).strip()
        team1_score = int(team1[-1])
        team2_score = int(team2[-1])
        team1 = (team1_name, team1_score)
        team2 = (team2_name, team2_score)
        return team1, team2


class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
    
    def __gt__(self, other):
        if self.points > other.points:
            return True
        elif self.points == other.points:
            return self.name < other.name
        return False
    
    def add_points(self, pts):
        self.points += pts