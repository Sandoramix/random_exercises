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

inputs = [
	"3[a]2[bc]",
	"3[a2[c]]",
	"1[2[a2[ci]]]"
]

solutions = [
	"aaabcbc",
	"accaccacc",
	"aciciacici"
]

# Write your code here --------------------------------------------------------

def solve(input: "str"):
	stack = []
	current_num = 0
	result = ""

	for c in input:
		if c.isdigit():
			current_num = current_num * 10 + int(c)
		elif c == "[":
			stack.append((result, current_num))
			result = ""
			current_num = 0
		elif c == "]":
			last_result, num = stack.pop()
			result = last_result + result * num
		else:
			result += c

	return result


#------------------------------------------------------------------------------
def run_and_test():
	if len(inputs) != len(solutions):
		print("Check inputs/solutions variables")
		exit(1)

	for idx, input in enumerate(inputs):
		result = solve(input)
		solution = solutions[idx]
		print(f"{idx}:\t", end="")
		if (result == solution):
			print("OK")
		else:
			print("KO")

def run():
	for idx, input in enumerate(inputs):
		result = solve(input)
		print(f"{idx} {{ input: {input},\tresult: {result},\tsolution: {solutions[idx]},\tmatch: {'OK' if result == solutions[idx] else 'KO'} }}")

if __name__ == "__main__":
	TEST=False
	if TEST:
		run_and_test()
	else:
		run()
