create table odds(
    odds_id serial primary key,
    game_id int,
    favourite varchar(100),
    spread float,
    total float
);
alter table odds owner to comp_user;

