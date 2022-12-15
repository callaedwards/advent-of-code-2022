from common import get_input_file_path
from typing import List, Dict, Tuple
from collections import defaultdict
from copy import deepcopy



class Stack:

	def reorg_stacks(self, stacks: List[str], directions: List[str]) -> str:
		self.ORIGINAL_STACK = self.parse_stacks(stacks)
		self.DIRECTIONS = self.parse_directions(directions)
		
		self.STACK1 = deepcopy(self.ORIGINAL_STACK)
		for direction in self.DIRECTIONS:
			self.move(direction)

		top_boxes = ""
		for s in range(1, 10):
			top_boxes += self.STACK1[s][-1]

		return top_boxes


	def reorg_stacks_2(self, stacks: List[str], directions: List[str]) -> str:
		self.STACK2 = deepcopy(self.ORIGINAL_STACK)
		
		for direction in self.DIRECTIONS:
			self.move_stack(direction)

		top_boxes = ""
		
		for s in range(1, 10):
			top_boxes += self.STACK2[s][-1]

		return top_boxes


	def parse_stacks(self, stacks: List[str]) -> Dict[int, str]:
		stack_dict = defaultdict(list)
		num_stacks = len(stacks[-1].replace(" ",""))
		stacks = [r.replace("    ","-").replace(" ", "").replace("[","").replace("]","") for r in stacks]
		for i in range(len(stacks) - 2, -1, -1):
			for j in range(num_stacks):
				if stacks[i][j] != "-":
					stack_dict[j+1] += stacks[i][j]
		return stack_dict


	def move(self, direction: Tuple[int, int, int]):
		num_boxes, start, destination = direction
		for _ in range(num_boxes):
			box = self.STACK1[start].pop()
			self.STACK1[destination].append(box)


	def parse_directions(self, directions: List[str]) -> List[Tuple[int, int, int]]:
		parsed_directions = []
		for i in range(len(directions)):
			d = directions[i].split()
			parsed_directions += [(int(d[1]), int(d[3]), int(d[5]))]
		return parsed_directions


	def move_stack(self, direction: Tuple[int, int, int]):
		num_boxes, start, destination = direction
		i = num_boxes * -1
		print(i)
		boxes = self.STACK2[start][i:]
		self.STACK2[start] = self.STACK2[start][:i]
		self.STACK2[destination] += boxes


def main():
	input_file = get_input_file_path("day5.txt")
	with open(input_file) as f:
		parsed_input = f.read().split("\n\n")
		stacks = parsed_input[0].split("\n")
		directions = parsed_input[1].split("\n")
	stack = Stack()
	c1 = stack.reorg_stacks(stacks, directions)
	c2 = stack.reorg_stacks_2(stacks, directions)
	print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
	main()
