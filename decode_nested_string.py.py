"""
Interviewer:
Write a program to give the following output for the given input

Example 1:
Input: "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: "3[a2[c]]"
Output: "accaccacc"
"""

#------------------------------------------------------------------------------

from curses.ascii import isdigit


inputs = [
	"3[a]2[bc]",
	# "3[a2[c]]"
]

solutions = [
	"aaabcbc",
	# "accaccacc"
]

def rec(s: "str"):
	# TODO
	return s

def solve(input: "str"):
	return rec(input)


#------------------------------------------------------------------------------
def run_and_test():
	if len(inputs) != len(solutions):
		print("Check inputs/solutions variables")
		exit(1)

	for idx, input in enumerate(inputs):
		result = solve(input)
		solution = solutions[idx]
		print(f"{idx}:\t", end="")
		if (result == solution): print("OK")
		else: print("KO")

def run():
	for idx, input in enumerate(inputs):
		result = solve(input)
		print(f"{idx}[{input}]:\t{result}")

if __name__ == "__main__":
	TEST=False
	if TEST: run_and_test()
	else: run()
