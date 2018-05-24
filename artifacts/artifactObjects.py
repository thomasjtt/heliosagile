class userstory:
	def __init__(self,user=None,goal=None,why=None):
		self.user = user
		self.goal = goal
		self.why = why

	def userstoryprinter():
		print 'As a {user}, I want {goal}, so that {why}'.format(user= self.user, goal=self.goal, why=self.why)
class productBacklog:
	pass

class sprintbook:
	pass

class sprint:
	pass

class burndown:
	pass