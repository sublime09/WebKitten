from . import Rubric

def getRubric():
	hw6 = Rubric.Rubric()
	hw6.addCrit("a", 1, -50, "You use forbidden functions.  Check the assignment requirements")
	hw6.addCrit("s", 1, -25, "You are not using any recursion.  Check the assignment requirements")
	hw6.addCrit("d", 1, -25, "You use ‘for’ or ‘while’ loops.  Check the assignment requirements")
	hw6.addCrit("f", 1, -10, "You solution is overly complex and quite hard to follow.  Use good commenting, good variables names, and concise code that clearly progresses towards the solution")
	hw6.addCrit("q", 2, -50, "You use forbidden functions.  Check the assignment requirements")
	hw6.addCrit("w", 2, -25, "You don't use any recursion.  Check the assignment requirements")
	hw6.addCrit("e", 2, -25, "You use ‘for’ or ‘while’ loops.  Check the assignment requirements")
	return hw6


'''
Allowed: print, str, int, float, bool, 
Allowed: len, list, range, abs, round, and pow

P1: -50 for using forbidden functions.  Check the assignment requirements
P1: -25 for not using any recursion.  Check the assignment requirements
P1: -25 for using ‘for’ or ‘while’ loops.  Check the assignment requirements
P1: -10 for a complex solution that is quite hard to follow.  Use good commenting, good variables names, and concise code that clearly progresses towards the solution

Good work!

P2: -50 for using forbidden functions.  Check the assignment requirements
P2: -25 for not using any recursion.  Check the assignment requirements
P2: -25 for using ‘for’ or ‘while’ loops.  Check the assignment requirements
P2: -10 for a complex solution that is quite hard to follow.  Use good commenting, good variables names, and concise code that clearly progresses towards the solution

Note: The 'in' keyword uses a normal loop, not recursion.  But there's no penalty for it in this case.  
Note: List functions (pop, append, remove, etc.) are not approved functions.  But there's no penalty for it in this case.  
Note: Avoid imports in your submission (You can turn off Eclipse's auto-import)
Note: You include other assignments in your webcat submission.  Make sure you are only submitting the code for HW6

Future Semester Notes:
Make allowed keywords list: if, elif, else, and, or, not, return, def, assert, 
Make a forbidden keywords list: for, while, in, import
Make allowed builtins list
'''