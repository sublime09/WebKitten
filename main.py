from pywinauto.application import Application
# Run a target application
# app = Application().start("notepad.exe")
# Select a menu item
# app.UntitledNotepad.menu_select("Help->About Notepad")
# Click on a button
# app.AboutNotepad.OK.click()
# Type a text string
# app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
# exit()

import pyperclip
import Rubrics.HW6

rubric = Rubrics.HW6.getRubric()

def main():
	usage = "Commands: exit, help, rubric, or a string of rubric keys"
	print(usage)
	userIn = ""
	while True:
		userIn = input("Input: ").strip().lower()
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
