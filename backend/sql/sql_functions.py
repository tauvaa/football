import os

from config import NFLDB_CREDS
from connections import Querier, run_commit_query, run_read_query
from utils import week_converter


def get_teams():
    query = """select distinct home_team from games"""
    to_ret = run_read_query(query)
    to_ret = [x[0] for x in to_ret]
    return to_ret


def get_team_stats(team):
    read_dir = os.path.join(os.path.dirname(__file__), "read")

    with open(os.path.join(read_dir, "wins.sql")) as f:
        wins_query = f.read()
    with open(os.path.join(read_dir, "losses.sql")) as f:
        losses_query = f.read()

    with open(os.path.join(read_dir, "ties.sql")) as f:
        ties_query = f.read()

    with open(os.path.join(read_dir, "home_covers.sql")) as f:
        home_covers = f.read()

    with open(os.path.join(read_dir, "away_covers.sql")) as f:
        away_covers = f.read()

    with open(os.path.join(read_dir, "spreads.sql")) as f:
        spreads = f.read()

    with Querier(NFLDB_CREDS) as querier:
        wins = querier.run_read_query(wins_query, {"team_name": team})
        wins = list(wins)[0][0]

        losses = querier.run_read_query(losses_query, {"team_name": team})
        losses = list(losses)[0][0]

        ties = querier.run_read_query(ties_query, {"team_name": team})
        ties = list(ties)[0][0]

        home_covers = querier.run_read_query(home_covers, {"team_name": team})
        home_covers = [x[0] for x in home_covers]
        home_covers = sum(home_covers)

        away_covers = querier.run_read_query(away_covers, {"team_name": team})
        away_covers = [x[0] for x in away_covers]
        away_covers = sum(away_covers)

        spreads = querier.run_read_query(spreads, {"team_name": team})
        spreads = [
            {
                "week": week_converter(x[0]),
                "odds_spread": x[1],
                "point_difference": x[2],
            }
            for x in spreads
        ]
        spreads.sort(key=lambda x: x["week"])

    return {
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "home_covers": home_covers,
        "away_covers": away_covers,
        "spreads": spreads,
    }


if __name__ == "__main__":
    r = get_team_stats("Rams")
    print(r)
