import os
import inspect

FILE_BASE= "input"
FILE_EXTENTION = "txt"

def get_input_file_path(filename: str):
	directory_name = os.path.abspath(os.path.join(os.getcwd(), "..", "inputs"))
	input_file_name = os.path.join(directory_name, filename)
	return input_file_name



# def run_all():
# 	dir_list = os.listdir(os.getcwd())
# 	dir_list.sort()
# 	for f in dir_list:
# 		if "day" in f:
# 			print(f)


# def main():
# 	run_all()