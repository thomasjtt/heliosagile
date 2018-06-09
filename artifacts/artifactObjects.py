lass productBacklog:
	def __init__(self,AgileAddressBook=None,sprintArchive=None,PBForms=None, taskArchive = None):
		self.AgileAddressBook = AgileAddressBook
		self.sprintArchive = sprintArchive
		self.PBForms = PBForms
		self.taskArchive = taskArchive

		print('inside the product backlog, objects loaded')


class userstory:
	def __init__(self,user=None,goal=None,why=None):
		self.user = user
		self.goal = goal
		self.why = why

	def userstoryprinter(self):
		print 'As a {user}, I want {goal}, so that {why}'.format(user= self.user, goal=self.goal, why=self.why)

class archSprint:
	def __init__(self):
		print('archSprint created')

class sprint:
	pass

class burndown:
	pass

class archTasks:
	def __init__(self):
		print('archTacks created')


# mongoimport -d agile -c users --type csv --file contactInfo.csv --headerline