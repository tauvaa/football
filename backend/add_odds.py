import os

from config import NFLDB_CREDS
from connections import Querier
from get_data import get_data


def get_game(week, home_team, away_team):
    with open(
        os.path.join(
            os.path.dirname(__file__), "sql", "read", "get_game_odds.sql"
        )
    ) as f:
        query = f.read()

    with Querier(NFLDB_CREDS) as q:
        game_id = q.run_read_query(query, (week, home_team, away_team))
        game_id = list(game_id)[0][0]
    return game_id


def add_odds():
    data = get_data()
    params = []
    for d in data:
        o = d.get("odd")
        home_odd, away_odd = o.get("home_odd"), o.get("away_odd")
        season_week = d.get("season_week")

        home_team = d.get("home_team").get("name")
        away_team = d.get("away_team").get("name")
        game_id = get_game(season_week, home_team, away_team)

        if home_odd == "N/A":
            continue

        try:
            float(home_odd)
            favourite = "home"

            spread = float(home_odd)
            total = away_odd
        except Exception as err:
            favourite = "away"
            spread = float(away_odd)
            total = home_odd
        if total != "N/A":

            total = float(total.split(":")[1])
        else:
            total = None
        params.append(
            {
                "game_id": game_id,
                "favourite": favourite,
                "spread": spread,
                "total": total,
            }
        )
    with open(
        os.path.join(os.path.dirname(__file__), "sql", "write", "odds.sql")
    ) as f:
        insert_query = f.read()
    with Querier(NFLDB_CREDS) as q:
        q.run_commit_query(insert_query, params=params, multi=True)


if __name__ == "__main__":
    add_odds()

    # print(home_odd, away_odd)
