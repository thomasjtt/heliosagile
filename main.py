# from addressBook.users import addressbook, employee
from artifacts.artifactObjects import userstory


def test_the_function(a, b):
    return a,b



if __name__ == "__main__":
    firstUserStory = userstory('frog', 'hops', 'go across the pond')

    firstUserStory.userstoryprinter()