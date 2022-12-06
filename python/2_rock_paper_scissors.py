from common import get_input_file_path
from typing import List, Tuple
from enum import Enum


"""
rock		X	A 		
paper 		Y 	B
scissors 	Z	C
"""

OUTCOMES = {'A': ('Z', 'X', 'Y'), 'B': ('X', 'Y', 'Z'), 'C': ('Y', 'Z', 'X')}
# opponent shape => (shape to lose, shape to tie, shape to win)


def calculate_score(guide: List[str]) -> int:
	score = 0
	for round in guide:
		score += calculate_win(round)
		if round[2] == "X":
			score += 1
		elif round[2] == "Y":
			score += 2
		else: #Z
			score += 3

	return score


def calculate_win(round: str) -> int:
	opponent = round[0]
	you = round[2]
	if ord(you) == ord(opponent) + 23:
		return 3
	elif (you == 'X' and opponent == 'C' or 
			you == 'Y' and opponent == 'A' or 
			you == 'Z' and opponent == 'B'):
		return 6
	else:
		return 0

def calculate_score_2(guide: List[str]) -> int:
	score = 0
	for round in guide:
		shape, outcome_score = calculate_shape(round)
		score += outcome_score
		round = round[:2] + shape

		if round[2] == "X":
			score += 1
		elif round[2] == "Y":
			score += 2
		else: #Z
			score += 3

	return score

def calculate_shape(round: str) -> Tuple[str, int]:
	opponent = round[0]
	outcome = round[2]
	if outcome == 'X': #lose
		return OUTCOMES[opponent][0], 0
	elif outcome == 'Y': #tie
	 	return OUTCOMES[opponent][1], 3
	else: # outcome == 'Z': #win
		return OUTCOMES[opponent][2], 6


def main():
	input_file = get_input_file_path("day2.txt")
	with open(input_file) as f:
		parsed_input = f.readlines()
	c1 = calculate_score(parsed_input)
	c2 = calculate_score_2(parsed_input)
	print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
	main()

