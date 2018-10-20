import pyperclip
import rubric

def main():
	userIn = ""
	while "exit" not in userIn.lower():
		userIn = input("Input here:")

		print("breaking loop!")
		break

	pyperclip.copy('The text to be copied to the clipboard.')
	cb = pyperclip.paste()
	print(cb)



if __name__ == '__main__':
	main()