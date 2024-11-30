import os
import importlib.util
import pathlib

class AOC:
    def __init__(self, year):
        self.year = year
        self.days = {}

    def load_days(self):
        base_path = f"./{self.year}"
        for day_folder in os.listdir(base_path):
            day_path = os.path.join(base_path, day_folder)
            if os.path.isdir(day_path):
                day_number = day_folder.replace("Day", "") 
                module_name = f"{day_folder}.day{day_number}"
                module_file = os.path.join(day_path, f"Day{day_number}.py")

                spec = importlib.util.spec_from_file_location(module_name, module_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                class_name = f"Day{day_number}"
                day_class = getattr(module, class_name) 
                self.days[day_number] = day_class 

    def run_day(self, day_number):
        if day_number in self.days:
            input_filename = f"{str(pathlib.Path(__file__).parent.resolve())}/{self.year}/Day{day_number}/input.txt"
            day_instance = self.days[day_number](filename=input_filename) 
            print(f"AdventOfCode\n\nEvent: {self.year}\nDay: {day_number}\n\n")
            print(f"Part-1: {day_instance.part1()}")
            print(f"Part-2: {day_instance.part2()}")
        else:
            print(f"Tag {day_number} nicht gefunden.")

if __name__ == "__main__":
    aoc = AOC(year="2023")
    aoc.load_days() 
    aoc.run_day("1")  
    #aoc.run_day("2")  
