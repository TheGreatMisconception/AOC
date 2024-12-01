import re
from pathlib import Path

class Day1:
    def __init__(self, filename="input.txt"):
        self.inputfile = Path(filename)
        self.read()
        self.parse_locations()


    def read(self) -> None:
        try:
            with self.inputfile.open() as file:
                self.input = {"raw": None, "lines": None}
                self.input["raw"] = file.read().strip()
                self.input["lines"] = self.input["raw"].split("\n")
        except FileNotFoundError:
            print(f"Error: The file {self.inputfile} was not found.")
            raise

    def parse_locations(self):
        self.parsed = list(map(str.split, self.input["lines"]))
        self.left = sorted(list(map(lambda x: int(x[0]), self.parsed)))
        self.right = sorted(list(map(lambda x: int(x[1]), self.parsed)))


    def calculate_part1(self) -> int:
        distances = [abs(value-self.right[index]) for index, value in enumerate(self.left)]
        return sum(distances)
        
    def calculate_part2(self) -> int:
        similarities = [self.right.count(i)*i for i in self.left]
        return(sum(similarities))

if __name__ == "__main__":
    day = Day1()
    print("AdventOfCode\n\nEvent:2024\nDay:1\n\n")
    print(f"Part-1: {day.calculate_part1()}")
    print(f"Part-2: {day.calculate_part2()}")

