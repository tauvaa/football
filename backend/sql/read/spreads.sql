select season_week,
case
	when (home_team = %(team_name)s and odds.favourite = 'home') or (away_team = %(team_name)s and odds.favourite = 'away')
	then odds.spread
	else
		-odds.spread
end odds_spread,
case
when home_team = %(team_name)s
	then home_team_score-away_team_score
else
	away_team_score - home_team_score
end point_difference
from games left join odds on games.game_id  = odds.game_id
where home_team = %(team_name)s
or away_team  = %(team_name)s
