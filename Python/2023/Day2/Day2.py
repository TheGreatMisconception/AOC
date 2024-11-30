import re
from pathlib import Path

class Day2:
    def __init__(self, filename="input.txt"):
        self.inputfile = Path(filename)
        self.max = {"red": 12, "blue": 14, "green": 13}
        self.read()
        self.games = self.parse_games(self.input["lines"])

    def read(self) -> None:
        try:
            with self.inputfile.open() as file:
                self.input = {"raw": None, "lines": None}
                self.input["raw"] = file.read().strip()
                self.input["lines"] = self.input["raw"].split("\n")
        except FileNotFoundError:
            print(f"Error: The file {self.inputfile} was not found.")
            raise

    def parse_games(self, gamelist: list) -> dict:
        games = {}
        for game_id_old, game in enumerate(gamelist):
            game_id, sets = game.split(":")
            game_id = int("".join(filter(str.isdigit, game_id)))
            
            red = max(map(int, re.findall(r'([1-9]|[1-9][0-9]).red', sets)))
            blue = max(map(int, re.findall(r'([1-9]|[1-9][0-9]).blue', sets)))
            green = max(map(int, re.findall(r'([1-9]|[1-9][0-9]).green', sets)))  
            games[game_id] = green * blue * red
        
        return(games)


    def calculate_part1(self) -> int:
        regex = r'^.*(([1-9][3-9]|[2-9][0-9]).red|([1-9][4-9]|[2-9][0-9]).green|([1-9][5-9]|[2-9][0-9]).blue).*\n'
        mod_list = re.sub(regex, "", self.input["raw"], count=0, flags=re.MULTILINE | re.IGNORECASE | re.VERBOSE).split("\n")
        return(sum(self.parse_games(mod_list).keys()))

    def calculate_part2(self) -> int:
      return(sum(self.games.values()))

if __name__ == "__main__":
    day = Day2()
    print("AdventOfCode\n\nEvent:2023\nDay:2\n\n")
    print(f"Part-1: {day.calculate_part1()}")
    print(f"Part-2: {day.calculate_part2()}")

