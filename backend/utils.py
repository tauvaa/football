def week_converter(weekstring):
    """Use to conver week from format YYYY-m to
    YYYY-MM. Ex: 2022-1 -> 2022-01"""
    year, week = weekstring.split("-")
    week = week if int(week) >= 10 else "0" + week
    return f"{week}"


if __name__ == "__main__":
    print(week_converter("2022-1"))
