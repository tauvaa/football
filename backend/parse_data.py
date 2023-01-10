import datetime as dt
from functools import reduce

from get_data import get_data


def parse_data(data):
    home_team, away_team = [
        data.get(x).get("name") for x in ("home_team", "away_team")
    ]
    score = data.get("box_score").get("score")
    home_score, away_score = [
        score.get(x).get("score") for x in ("home", "away")
    ]
    start_time = data.get("game_date")
    # start_time = start_time.split(" ")
    start_time = dt.datetime.strptime(start_time, "%a, %d %b %Y %H:%M:%S %z")
    start_time -= dt.timedelta(hours=6)
    start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

    to_ret = {
        "home_team": home_team,
        "away_team": away_team,
        "home_score": home_score,
        "away_score": away_score,
        "start_time": start_time,
        "season_week": data.get("season_week"),
    }

    return to_ret


if __name__ == "__main__":
    data = get_data()
    for d in data:
        print(parse_data(d))
