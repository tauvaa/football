from os import wait

from flask import Flask, request
from flask_cors import CORS

import sql.sql_functions as sql

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "hello world!"


@app.route("/teams", methods=["GET"])
def get_teams():
    teams = sql.get_teams()
    teams.sort()
    return {"teams": teams}


@app.route("/teamstats", methods=["GET"])
def get_team_stats():
    team = request.args.get("team")
    stats = sql.get_team_stats(team)
    return stats


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
