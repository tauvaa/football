select season_week,
case
	when (home_team = 'Rams' and odds.favourite = 'home') or (away_team = 'Rams' and odds.favourite = 'away')
	then odds.spread
	else
		-odds.spread
end odds_spread,
case 
when home_team = 'Rams'
	then home_team_score-away_team_score
else
	away_team_score - home_team_score
end point_difference
from games left join odds on games.game_id  = odds.game_id
where home_team = 'Rams'
or away_team  = 'Rams'
