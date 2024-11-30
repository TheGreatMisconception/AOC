import re

class Day1():
    def __init__(self, filename="input.txt"):
        self.inputfile = filename
        self.input = {"lines": "", "raw": ""}
        self.read()

    def read(self):
        with open(self.inputfile) as file:
            self.input["raw"] = file.read()[:-1]
            self.input["lines"] = self.input["raw"].split("\n")

    def part1(self):
        calibration_values = re.sub("[a-z]", "", self.input["raw"]).split("\n")
        calibration_values = list(map(lambda s: int(f"{s[0]}{s[-1]}"), calibration_values))
        return sum(calibration_values)

    def part2(self):
        calibration_values = []
        numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
        
        for key, line in enumerate(self.input["lines"]):
            digits = []
            rank =  {}
            
            for number in numbers:
                digits += sorted([i.start() for i in re.finditer(str(number), line)])
                res = sorted([i.start() for i in re.finditer(numbers[number], line)])
                if len(res) > 0: rank[res[0]], rank[res[-1]] = number, number
            
            calibration_value = line
            
            if len(rank.keys()) > 0:
                positions = sorted(rank.keys())
                first, last = positions[0], positions[-1]
                if len(digits) == 0 or first < digits[0]:
                    calibration_value = line.replace(numbers[rank[first]], str(rank[first]),1)
                if len(digits) == 0 or last > digits[-1]:
                    calibration_value = calibration_value.replace(numbers[rank[last]], str(rank[last]))
            
            calibration_value = re.sub("[a-z]", "", calibration_value)
            calibration_values.append(int(f"{calibration_value[0]}{calibration_value[-1]}"))
        
        return (sum(calibration_values))
            
        
if __name__ == "__main__":

    Day = Day1()
    print("AdventOfCode\n\nEvent:2023\nDay:1\n\n")
    print(f"Part-1: {Day.part1()}")
    print(f"Part-2: {Day.part2()}")

