insert into games(
home_team,
away_team,
home_team_score,
away_team_score,
game_time,
season_week
)
values(
    %(home_team)s,
    %(away_team)s,
    %(home_score)s,
    %(away_score)s,
    %(start_time)s,
    %(season_week)s
)
