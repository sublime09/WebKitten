import pyperclip
import Rubrics.HW6

rubric = Rubrics.HW6.getRubric()

def main():
	usage = "Commands: exit, help, rubric, or a string of rubric keys"
	print(usage)
	userIn = ""
	while True:
		userIn = input("Input: ").lower().strip()
		if "exit" in userIn:
			break
		elif "help" in userIn:
			print(usage)
			print("Enter 'exit' to exit at any time.")
		elif 'rubric' in userIn:
			print(rubric)
		else:
			comment = []
			for c in userIn:
				comment.append(rubric.get(c))
			comment = '\n'.join(comment)
			pyperclip.copy(comment)
			print("Copied to clipboard:")
			print(comment)
			print()


if __name__ == '__main__':
	main()
