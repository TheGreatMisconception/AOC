import re
from pathlib import Path

class Day1:
    def __init__(self, filename="input.txt"):
        self.inputfile = Path(filename)
        self.input = {"lines": [], "raw": ""}
        self.read()

    def read(self) -> None:
        try:
            with self.inputfile.open() as file:
                self.input["raw"] = file.read().strip()
                self.input["lines"] = self.input["raw"].split("\n")
        except FileNotFoundError:
            print(f"Error: The file {self.inputfile} was not found.")
            raise

    def calculate_part1(self) -> int:
        calibration_values = re.sub("[a-z]", "", self.input["raw"]).split("\n")
        calibration_values = list(map(lambda s: int(f"{s[0]}{s[-1]}"), calibration_values))
        return sum(calibration_values)

    def calculate_part2(self) -> int:
        numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
        calibration_values = []

        for line in self.input["lines"]:
            digits = [i.start() for i in re.finditer(r'\d', line)]
            rank = {}

            for number, word in numbers.items():
                positions = [i.start() for i in re.finditer(word, line)]
                if positions:
                    rank[positions[0]] = number
                    rank[positions[-1]] = number

            calibration_value = line
            if rank:
                positions = sorted(rank.keys())
                first, last = positions[0], positions[-1]
                if not digits or first < digits[0]:
                    calibration_value = calibration_value.replace(numbers[rank[first]], str(rank[first]), 1)
                if not digits or last > digits[-1]:
                    calibration_value = calibration_value.replace(numbers[rank[last]], str(rank[last]))

            calibration_value = re.sub("[a-z]", "", calibration_value)
            calibration_values.append(int(f"{calibration_value[0]}{calibration_value[-1]}"))

        return sum(calibration_values)

if __name__ == "__main__":
    day = Day1()
    print("AdventOfCode\n\nEvent:2023\nDay:1\n\n")
    print(f"Part-1: {day.calculate_part1()}")
    print(f"Part-2: {day.calculate_part2()}")

