from common import get_input_file_path
from typing import List


def find_subsets(pairs: List[List[str]]):
	count = 0
	for pair in pairs:
		ranges = parse_pair_to_ints(pair)
		count += is_subset(ranges)
	return count

def find_overlap(pairs: List[List[str]]):
	count = 0
	for pair in pairs:
		ranges = parse_pair_to_ints(pair)
		if ranges[0] >= ranges[2] and ranges[0] <= ranges[3]:
			count += 1
		elif ranges[1] >= ranges[2] and ranges[1] <= ranges[3]:
			count += 1
		else:
			count += is_subset(ranges)

	return count

def is_subset(ranges: List[int]) -> int:
	if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
		return 1
	elif ranges[0] >= ranges[2] and ranges[1] <= ranges[3]:
		return 1
	return 0

def parse_pair_to_ints(pair: List[str]):
	return [int(y) for p in pair for y in p.split("-")]

def main():
	input_file = get_input_file_path("day4.txt")
	with open(input_file) as f:
		parsed_input = f.readlines()
		pairs = [p.split(",") for p in parsed_input]
	c1 = find_subsets(pairs)
	c2 = find_overlap(pairs)
	print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
	main()

# 1-9 2-5
# 3-9 1-3
#
#
#
#

