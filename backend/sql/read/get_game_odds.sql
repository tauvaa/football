select game_id 
from games 
where
    season_week = %s 
    and home_team = %s
    and away_team = %s
