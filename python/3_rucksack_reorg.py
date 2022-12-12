from common import get_input_file_path
from typing import List


def find_duplicate(rucksacks: List[str]) -> int:
	priority = 0
	for sack in rucksacks:
		midpoint = len(sack)//2
		for item in sack[0: midpoint]:
			if item in sack[midpoint:]:
				duplicate = item
				break
		priority += calculate_priority(duplicate)

	return priority

def calculate_priority(item: str) -> int:
	if ord(item) >= 97:
		return ord(item) - 96
	else:
		return ord(item) - 38


def find_duplicate_in_3(rucksacks: List[str]) -> int:
	priority = 0
	for sack in range(0, len(rucksacks), 3):
		for item in rucksacks[sack]:
			if item in rucksacks[sack + 1] and item in rucksacks[sack + 2]:
				badge = item
				break
		priority += calculate_priority(badge)

	return priority



def main():
	input_file = get_input_file_path("day3.txt")
	with open(input_file) as f:
		parsed_input = f.readlines()
	c1 = find_duplicate(parsed_input)
	c2 = find_duplicate_in_3(parsed_input)
	print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
	main()

