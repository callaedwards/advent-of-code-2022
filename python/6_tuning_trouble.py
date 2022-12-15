from common import get_input_file_path



def find_marker(buffer: str) -> int:
	for i in range(len(buffer) - 3):
		if len(set(buffer[i:(i + 4)])) == 4:
			return i + 4


def find_marker_2(buffer: str) -> int:
	for i in range(len(buffer) - 13):
		if len(set(buffer[i:(i + 14)])) == 14:
			return i + 14


def main():
	input_file = get_input_file_path("day6.txt")
	with open(input_file) as f:
		parsed_input = f.read()
	c1 = find_marker(parsed_input)
	c2 = find_marker_2(parsed_input)
	print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
	main()
