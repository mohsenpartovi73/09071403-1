def sort(teams):
    teams.sort(key=lambda x: (-x[1], -x[4], x[0]))


def printer(teams):
    for team in teams:
        print(team[0], team[1], team[2], team[3], team[4])


teams = []
for i in range(2):
    team_name = input("team name : ")
    team_win = int(input("number of match wins : "))
    team_loses = int(input("number of match lose:"))
    team_goal_diffrences = int(input("number of goal diffrences:"))
    team_score = team_win * 3
    teams.append((team_name, team_score, team_win, team_loses, team_goal_diffrences))
sort(teams)
printer(teams)
