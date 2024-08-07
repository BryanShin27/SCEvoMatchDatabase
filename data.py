import datetime

class Series:
    """
    A class used to represent ONE Best-of-X Match Series
    """
    def _init_(self, matches)
        # pointers to matches

class Match:
    """
    A class used to represented ONE game (ONE map played)
    """
    def __init__(self, player_one: str, player_two: str, date: datetime.date, result: int)
        self.player_one = player_one
        self.player_two = player_two
        self.date = date
        self.result = result

    def set_player_one(player_one: str):
        self.player_one = player_one

    def set_player_two(player_two: str):
        self.player_two = player_two

    def set_date(date: str):
        self.date = date

    def set_result(result: str):
        self.result = result

class Player:
    """
    A class used to represent ONE player
    """
    def __init__(self, name: str, alias: list, age: int, race: str, flag: str):
        self.name = name
        self.alias = alias
        self.age = age
        self.race = race
        self.flag = flag
        
    def set_name(self, name):
        self.name = name

    def set_alias(self, alias)
        self.alias.append(alias)

    def set_race(self, race):
        self.race = race

    def set_flag(flag):
        self.flag = flag

class Map:
    """
    A class used to represent ONE map
    """
    def _init(self, name: str, name_full: str, height: str, width: str, author: str):
        self.name = name

class 