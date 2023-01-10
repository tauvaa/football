import os

from connections import run_commit_query, run_read_query


def get_teams():
    query = """select distinct home_team from games"""
    to_ret = run_read_query(query)
    to_ret = [x[0] for x in to_ret]
    return to_ret


def get_team_stats(team):
    read_dir = os.path.join(os.path.dirname(__file__), "read")

    with open(os.path.join(read_dir, "wins.sql")) as f:
        wins_query = f.read()
    wins = run_read_query(wins_query, {"team_name": team})
    wins = list(wins)[0][0]
    with open(os.path.join(read_dir, "losses.sql")) as f:
        losses_query = f.read()
    losses = run_read_query(losses_query, {"team_name": team})
    losses = list(losses)[0][0]
    return {"wins": wins, "losses": losses}


if __name__ == "__main__":
    print(get_team_stats("Rams"))
