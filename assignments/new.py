import pdb
#pdb.set_trace()


class People:

    def __init__(self, name, nextPeople=None, prvPeople=None):
        self.name = name
        self.nextPeople = nextPeople
        self.prvPeople = prvPeople

    def getNextPeople(self):
        return self.nextPeople

    def getPrevPeople(self):
        return self.prvPeople

    def setNextNode(self, name):
        self.nextPeople = name


class PeopleList:

    def __init__(self, head=None, first=None):
        self.head = head
        self.first = first
        self.size = 0

    def getSize(self):
        return self.size

    def addPeople(self, name):
        newPeople = People(name, self.head, None)
        temp = self.head

        if self.head is not None:
            newPeople.prvPeople = self.first
            temp.prvPeople = newPeople
            while (temp.nextPeople != self.head):
                prev = temp
                temp = temp.nextPeople
                temp.prvPeople = prev

            temp.nextPeople = newPeople

        else:
            newPeople.nextPeople = newPeople
            newPeople.prvPeople = newPeople

        self.size += 1
        self.head = newPeople

        if self.first is None:
            self.first = newPeople

        return True

    def printPeopleNext(self):
        curr = self.head
        while True:
            print(curr.name)
            if curr.nextPeople == self.head:
                break
            else:
                curr = curr.nextPeople

    def printPeoplePrev(self):
        curr = self.first
        while True:
            print(curr.name)
            if curr.prvPeople == self.first:
                break
            else:
                curr = curr.getPrevPeople()

    def killFromRight(self):
        curr = self.first
        while curr.prvPeople is not curr.nextPeople:
            if curr.prvPeople.prvPeople:
                print("%s will be kill" % (curr.prvPeople.name))
                curr.prvPeople = curr.prvPeople.prvPeople
                curr.prvPeople.prvPeople.nextPeople = curr
                curr = curr.prvPeople
                print("swords passed to %s" % (curr.name))
            else:
                curr.prvPeople = curr.prvPeople
                curr.nextPeople = curr.prvPeople

        print("finally %s will alive " % (curr.name))

    def killFromLeft(self):
        curr = self.first
        while curr.prvPeople is not curr.nextPeople:
            if curr.nextPeople.nextPeople:
                print("%s will be kill" % (curr.nextPeople.name))
                curr.nextPeople = curr.nextPeople.nextPeople
                curr.nextPeople.nextPeople.prvPeople = curr
                curr = curr.nextPeople
                print("swords passed to %s" % (curr.name))
            else:
                curr.prvPeople = curr.prvPeople
                curr.nextPeople = curr.prvPeople

        print("finally %s will alive " % (curr.name))


people_list = PeopleList()
people_list2 = PeopleList()
print("Inserting")
try:
    number = int(input("Enter a number :-"))
    for n in range(number):
        people_list.addPeople(n)
    print("Printing from Right............")
    people_list.printPeoplePrev()
    print("Printing from Left.............")
    people_list.printPeopleNext()
    print("Deletion from Right............")
    people_list.killFromRight()
    for n in range(number - 1):
        people_list2.addPeople(n)
    print("Deletion from Left.............")
    people_list2.killFromLeft()
except ValueError:
    print("Sorry this is not a valid number")







