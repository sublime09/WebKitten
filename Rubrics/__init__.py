class Rubric:
    def addCrit(self, key, problem, penalty, comment):
        if not hasattr(self, "crits"):
            self.crits = dict()
        c = Criteria()
        c.key = key
        c.problem = problem
        c.penalty = penalty
        c.comment = comment
        self.crits[key] = c

    def get(self, key):
        return repr(self.crits[key])

    def __repr__(self):
        s = ["Rubric key :: comment"]
        for k, v in self.crits.items():
            s.append("{} :: {}".format(k, v))
        return '\n'.join(s)

class Criteria:
    def __repr__(self):
        assert self.problem, "Problem not assigned"
        assert self.penalty, "Penalty not assigned"
        assert self.comment, "Comment not assigned"
        comm = self.comment
        # comm = (comm[:75] + '...') if len(comm) > 75 else comm
        args = (self.problem, self.penalty, comm)
        return "P{}: {}pts: {}".format(*args)

def getHW6():
    hw6 = Rubric()
    hw6.addCrit("a", 1, -50, "You use forbidden functions.  Check the assignment requirements")
    hw6.addCrit("s", 1, -25, "You are not using any recursion.  Check the assignment requirements")
    hw6.addCrit("d", 1, -25, "You use ‘for’ or ‘while’ loops.  Check the assignment requirements")
    hw6.addCrit("f", 1, -10, "You solution is overly complex and quite hard to follow.  Use good commenting, good variables names, and concise code that clearly progresses towards the solution")
    hw6.addCrit("q", 2, -50, "You use forbidden functions.  Check the assignment requirements")
    hw6.addCrit("w", 2, -25, "You don't use any recursion.  Check the assignment requirements")
    hw6.addCrit("e", 2, -25, "You use ‘for’ or ‘while’ loops.  Check the assignment requirements")
    return hw6

if __name__ == '__main__':
    myR = Rubric()
    myR.addCrit("k", 1, -5, "problem???")
    myR.addCrit("l", 1, -5, "problem")
    myR.addCrit("m", 1, -5, "PROBLEM")
    print(myR)
    hw6.addCrit("r", 2, -10, "You solution is overly complex and quite hard to follow.  Use good commenting, good variables names, and concise code that clearly progresses towards the solution")
    