import random
doors=[]
rightDoor=0
chosenDoor=0
removedDoor=0
wins=0

def setup():
    global doors, leftDoor, rightDoor, chosenDoor, removedDoor, wins

    doors = [1, 2, 3]

    rightDoor = random.randint(1, 3)
    chosenDoor = random.randint(1, 3)

    # print("rightDoor: ", rightDoor)
    # print("chosenDoor: ", chosenDoor)

    doors.remove(chosenDoor)
    try:
        doors.remove(rightDoor)
    except ValueError:
        pass  


    removedDoor = random.choice(doors)
    # print("it is not in room ", removedDoor)
    doors.remove(removedDoor)



def switchDoor():
    global doors, leftDoor, rightDoor, chosenDoor, removedDoor, wins

    doors.append(rightDoor)

    try:
        doors.remove(chosenDoor)
    except ValueError:
        doors = doors


    # print("i choose door", doors[0], "\n")
    chosenDoor = doors[0]


def check():
    global doors, leftDoor, rightDoor, chosenDoor, removedDoor, wins

    if chosenDoor == rightDoor:
        wins+=1


for i in range(0, 40):
    setup()
    check()

print("win percent of keeping door:", wins/40)

wins=0

for i in range(0, 40):
    setup()
    switchDoor()
    check()

print("win percent of switching door:", wins/40)






# Randomly choose right door
# Randomly choose a door

# Randomly choose a door that isn't the right one nor the one they chose and reveal that nothing is in it
# make them switch from the door they chose to the other door