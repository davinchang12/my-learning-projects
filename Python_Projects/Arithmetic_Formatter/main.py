def arithmetic_arranger(problems, ans=False):

	first = ''
	second = ''
	lines = ''
	answers = ''
	arranged_problems = ''

	if len(problems) > 5:
		return "Error: Too many problems."
	else:
		for i in range(len(problems)):
			text = problems[i].split()
			first_prob = text[0]
			second_prob = text[2]
			operator_prob = text[1]
			# print(operator_prob)
			
			if not(first_prob.isdigit()) or not(second_prob.isdigit()):
				return "Error: Numbers must only contain digits."

			if len(first_prob) > 4 or len(second_prob) > 4:
				return "Error: Numbers cannot be more than four digits."

			if operator_prob == "+" or operator_prob == '-':
				length = max(len(first_prob), len(second_prob)) + 2
				top = str(first_prob).rjust(length)
				bottom = operator_prob + str(second_prob).rjust(length-1)
				space = ' '*4
				line = '-'*length
				if(operator_prob == "+"):
					answer = str(int(first_prob) + int(second_prob)).rjust(length)
				else:
					answer = str(int(first_prob) - int(second_prob)).rjust(length)
			else:
				return "Error: Operator must be '+' or '-'." 	

			if(i < len(problems)-1):
				first += top + space
				second += bottom + space
				lines += line + space
				answers += answer + space 
			else:
				first += top
				second += bottom
				lines += line
				answers += answer

		first.rstrip()
		second.rstrip()
		lines.rstrip()
		answers.rstrip()

		if(ans):
			arranged_problems = first + '\n' + second + '\n' + lines + '\n' + answers
		else:
			arranged_problems = first + '\n' + second + '\n' + lines
 		

	return arranged_problems

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))