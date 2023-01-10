select count(*) from games
where ((home_team  = %(team_name)s
and home_team_score <away_team_score)
or (away_team = %(team_name)s and away_team_score < home_team_score)
);
