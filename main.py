# from addressBook.users import addressbook, employee
from artifacts.artifactObjects import productBacklog
from artifacts.artifactObjects import archSprint
from artifacts.smallerArtifacts import formBank
from artifacts.artifactObjects import archTasks
from addressBook.users import addressbook
from artifacts.artifactObjects import userstory

def test_the_function(a, b):
	return a,b



if __name__ == "__main__":
	firstUserStory = userstory('frog', 'hops', 'go across the pond')
	firstUserStory.userstoryprinter()

	print('creating product backlog')

	AgileAddressBook = addressbook()
	sprintArchive = archSprint()
	PBForms = formBank()
	taskArchive = archTasks()

	productBacklog = productBacklog(AgileAddressBook,sprintArchive,PBForms,taskArchive)