# practice_4


Iran = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
Spain = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
Morocco = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
Portugal = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}


def game(team1, team2):
    Iran = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
    Spain = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
    Morocco = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
    Portugal = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
    Team1 = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
    Team2 = {"win": 0, "loses": 0, "draws": 0, "goal_diffrences": 0, "points": 0}
    if team1 > team2:
        Team1["points"] = 3
        Team1["win"] = 1
        Team2["loses"] = 1
    elif team1 == team2:
        Team1["draws"] = 1
        Team2["draws"] = 1
    elif team1 < team2:
        Team2["points"] = 3
        Team2["win"] = 1
        Team1["loses"] = 1

    Iran = Team1
    Spain = Team2
    print(Iran)
    print(Spain)
