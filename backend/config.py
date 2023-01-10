import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

NFLDB_CREDS = {

    x: os.getenv(f"nfl_{x}") for x in "database password user host port".split()
}


if __name__ == "__main__":
    print(NFLDB_CREDS)
