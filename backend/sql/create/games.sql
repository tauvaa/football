create table if not exists games(
    game_id serial primary key,
    home_team varchar(100),
    away_team varchar(100),
    home_team_score int,
    away_team_score int,
    game_time timestamp,
    season_week varchar(25)

);
alter table games owner to comp_user;
alter sequence games_game_id_seq owner to comp_user;
