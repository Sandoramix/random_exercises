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
	s_len = len(s)
	opening_idx = s.index("[")

	opening_count = 1
	end_idx = opening_idx + 1
	while (opening_count != 0 and end_idx < s_len):
		if (s[end_idx] == '['):
			opening_count += 1
		if (s[end_idx] == ']'):
			opening_count -= 1
		if (opening_count > 0):
			end_idx += 1

	text = ""
	number_end = opening_idx - 1
	while (number_end >= 0 and not s[number_end].isdigit()):
		text = text + s[number_end]
		number_end += 1

	text += rec(s[opening_idx + 1:end_idx])

	if number_end < 0: return text
	n = int(s[:number_end])
	text = text * n
	return text

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
