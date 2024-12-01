import re
from pathlib import Path

class Day3:
    def __init__(self, filename="input.txt"):
        self.inputfile = Path(filename)
        self.parts = []
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

    def is_symbol_nearby(self, pos, arr) -> bool:
        pos_comb = [[pos[0]+1,pos[1]], [pos[0]-1,pos[1]], [pos[0],pos[1]+1], [pos[0],pos[1]-1], [pos[0]+1,pos[1]-1], [pos[0]+1,pos[1]+1], [pos[0]-1,pos[1]-1], [pos[0]-1,pos[1]+1]]
        for position in pos_comb:
            try:
                if not arr[position[0]][position[1]].isdigit() and arr[position[0]][position[1]] != ".":
                    return(True)
            except IndexError as e:
                #print(e)
                continue
        return False

    def check_number(self, number, positions, arr):
        for pos in positions:
            if self.is_symbol_nearby(pos, arr):
                self.parts.append(number)
                break
        
    def calculate_part1(self) -> int:
        arr = [list(i) for i in self.input["lines"]]
        for y in range(len(arr)):
            num, num_positions = "", []
            for x in range(len(arr[0])):
                if arr[y][x].isdigit():
                    num += arr[y][x]
                    num_positions.append([y,x])
                if len(num) > 0 and not arr[y][x].isdigit():
                    self.check_number(int(num), num_positions, arr)
                    num = ""
                    num_positions = []
                    
            if len(num) > 0: 
                self.check_number(int(num), num_positions, arr)
                
        return(sum(self.parts))

    def calculate_part2(self) -> int:
      return(0)

if __name__ == "__main__":
    day = Day3()
    print("AdventOfCode\n\nEvent:2023\nDay:3\n\n")
    print(f"Part-1: {day.calculate_part1()}")
    print(f"Part-2: {day.calculate_part2()}")

