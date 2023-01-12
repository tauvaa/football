with temp as (
select
	away_team_score - home_team_score score_diff,
	odds.favourite,
	odds.spread,
	games.home_team,
	games.away_team,
	games.home_team_score,
	games.away_team_score  
from odds join games on odds.game_id = games.game_id
where (games.away_team = %(team_name)s))
select case
	when favourite = 'home' and score_diff - spread > 0
		then 1
	when favourite = 'home' and score_diff - spread < 0
		then 0
	when favourite = 'away' and score_diff + spread > 0
		then 1
	else
		0
end
from temp
