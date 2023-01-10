from connections import write_games
from parse_data import parse_data
from get_data import get_data

if __name__ == "__main__":
    data = get_data()
    for d in data:
        print(parse_data(d))
        write_games(parse_data(d))
