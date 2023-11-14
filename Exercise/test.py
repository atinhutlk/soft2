class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
def checkClassroom(classroom):
    if len(classroom) == 0:
        print(f'Class is empty')
    else:
        for person in classroom:
            print(f'Name: {person.name}, Height : {person.height}')

    tallest_height = 0
    tallest_person = None

    for person in classroom:
        if person.height > tallest_height:
            tallest_height = person.height
            tallest_person = person
    if tallest_person:
        print(f"The tallest person is: {tallest_person.name}")
        classroom.remove(tallest_person)
        print(f"{tallest_person.name} has been removed from the classroom.")
classroom = []

while True:
    name = input("Enter student's name (or press Enter to finish): ")
    if not name:
        break
    height = int(input("Enter student's height in cm: "))
    person = Person(name, height)
    classroom.append(person)


checkClassroom(classroom)