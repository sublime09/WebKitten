class Rubric:
	def __init__(self):
		self.crits = dict()

	def addCriteria(self, key, problem, penalty, comment):
		c = Criteria()
		# c.key = key
		c.problem = problem
		c.penalty = penalty
		c.comment = comment
		self.crits[key] = c

	def __repr__(self):
		s = []
		for k, v in self.crits.items():
			s.append("{} :: {}".format(k, v))
		return '\n'.join(s)

class Criteria:
	def __repr__(self):
		assert self.problem, "Problem not assigned"
		assert self.penalty, "Penalty not assigned"
		assert self.comment, "Comment not assigned"
		args = (self.problem, self.penalty, self.comment)
		return "P{}: {}pts: {}".format(*args)

r = Rubric()
r.addCriteria("k", 1, -5, "problem???")
r.addCriteria("l", 1, -5, "problem")
r.addCriteria("m", 1, -5, "PROBLEM")

print(r)

