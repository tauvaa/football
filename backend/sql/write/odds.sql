insert into odds(
    game_id,
    favourite,
    spread,
    total
)
values(
    %(game_id)s,
    %(favourite)s,
    %(spread)s,
    %(total)s
)
