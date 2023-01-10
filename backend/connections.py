import os

import psycopg2 as psy

from config import NFLDB_CREDS


class Connector:
    def __init__(self, creds) -> None:
        self.creds = creds
        self.connection: psy.extensions.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting")
        self.connection.close()

    def __enter__(self):
        self.connection = psy.connect(**self.creds)
        return self


class Querier(Connector):
    def __init__(self, creds) -> None:
        super().__init__(creds)

    def run_read_query(self, query, params=None, with_cols=False):
        params = params or ()
        cur = self.connection.cursor()
        cur.execute(query, params)
        cols = [x.name for x in cur.description]
        to_yield = cur.fetchone()
        while to_yield:
            if with_cols:
                to_yield = dict(zip(cols, to_yield))
            yield to_yield
            to_yield = cur.fetchone()

    def run_commit_query(self, query, params=None, multi=False):
        params = params or ()
        cur = self.connection.cursor()
        if multi:
            cur.executemany(query, params)
        else:
            cur.execute(query, params)
        self.connection.commit()

    def __enter__(self):
        super().__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)


def run_read_query(query, params=None, with_cols=False, creds=NFLDB_CREDS):
    params = params or ()
    con = psy.connect(**creds)
    try:
        cur = con.cursor()
        cur.execute(query, params)
        cols = [x.name for x in cur.description]
        to_yield = cur.fetchone()
        while to_yield:
            if with_cols:
                to_yield = dict(zip(cols, to_yield))
            yield to_yield
            to_yield = cur.fetchone()

    finally:
        con.close()


def run_commit_query(query, params=None, multi=False, creds=NFLDB_CREDS):
    params = params or ()
    con = psy.connect(**creds)

    try:
        cur = con.cursor()
        if multi:
            cur.executemany(query, params)
        else:

            cur.execute(query, params)
        con.commit()

    finally:
        con.close()


def write_games(game_dict):
    with open(
        os.path.join(os.path.dirname(__file__), "sql", "write", "games.sql")
    ) as f:
        query = f.read()
    run_commit_query(query, game_dict)


if __name__ == "__main__":
    with Querier(NFLDB_CREDS) as connection:

        query = """select * from games where home_team=%s"""
        data = list(connection.run_read_query(query, params=("Rams",)))
        print(data)
