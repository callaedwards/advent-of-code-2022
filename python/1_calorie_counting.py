from common import get_input_file_path
from typing import List


def find_max_calories(elves: List[List[int]]) -> int:
	return max(sum_calories(elves))


def sum_calories(elves: List[List[int]]) -> List[int]:
	return [sum(elf) for elf in elves]


def find_top_3_calories(elves: List[List[int]]) -> int:
	calorie_list = sum_calories(elves)
	total = 0
	for _ in range(3):
		max_calories = max(calorie_list)
		total += max_calories
		calorie_list.remove(max_calories)
	return total


def main():
	input_file = get_input_file_path("day1.txt")
	with open(input_file) as f:
		parsed_input = f.read().split("\n\n")
	elves = [[int(l) for l in line.split()] for line in parsed_input]
	c1 = find_max_calories(elves)
	c2 = find_top_3_calories(elves)
	print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
	main()