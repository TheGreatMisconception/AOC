import re
from pathlib import Path

class Day2:
    def __init__(self, filename="input.txt"):
        self.inputfile = Path(filename)
        self.read()


    def read(self) -> None:
        try:
            with self.inputfile.open() as file:
                self.input = {"raw": None, "lines": None}
                self.input["raw"] = file.read().strip()
                self.input["lines"] = self.input["raw"].split("\n")
        except FileNotFoundError:
            print(f"Error: The file {self.inputfile} was not found.")
            raise


    def is_safe_report(self, report: list) -> str:
        increasing = decreasing = safe = True

        for key, level in enumerate(report[1:], start=1):
            if not (abs(level-report[key-1]) >= 1 and abs(level-report[key-1]) <= 3):
                safe = False
                break
            elif level > report[key - 1]: 
                decreasing = False
            elif level < report[key - 1]: 
                increasing = False
                
        return True if (increasing or decreasing) and safe else False


        

    def calculate_part1(self) -> int:
        reports = [i for i in map(lambda x: list(map(int, x.split())),self.input["lines"]) if self.is_safe_report(i)]
        return len(reports)
            
            
    def calculate_part2(self) -> int:
        return 0

        
if __name__ == "__main__":
    day = Day2()
    print("AdventOfCode\n\nEvent:2024\nDay:2\n\n")
    print(f"Part-1: {day.calculate_part1()}")
    print(f"Part-2: {day.calculate_part2()}")

