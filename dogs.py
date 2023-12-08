# Name: Kevin Merchancano
# Prog Puropose: This programe demostrates how to manipulte a list, including:
#   Finding number of items in the list, sorting the list, adding/removing items,
#   copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle",
        "Gonzo", "Sweetie-Pie", "Diego"]
dogs2 = []

def main():
    how_many = len(dogs)
    print("\nNumber of dogs in the list: " + str(how-many))
    print("\nOriginal list of dogs names:")
    print(dogs)

    dogs.reverse()
    print("\nList from last to first:")
    print(dogs)

    dogs.sort()
    print("\nAlphabetized list:")
    print(dogs)

    dogs.sort(reverse = True)
    print("\nLoist in reversed alphabetized order:")
    print(dogs)

    dogs.append("Ranger")
    print("\nAdd a dog to the end of the list:")
    print(dogs)

    doggy = dogs.pop(0)
    print("\nPop a dog off (remove) from the from of the list:")
    print(dogs)
    print(doggy + " was removed from the front of the list.")

    another_dog = dogs.pop(3)
    print("\nNote: Position numbers in a list begin with 0, not with 1")
    print(dogs)

    print(another_dog + " was removed from positions 3 of the list.")

    dogs.remove('AnnaBelle')
    print("\nRemove a dog by name rather than position in the list:")
    print(dogs)

    dogs2 = dog
    print("\nA list can be copied into another list by setting one equal to the other:")
    print(dogs)
    print(dogs2)

    print("\nUse a FOR loop to gove each dog in the same last name:")
    for i in range(len(dogs)):
        dogs[i] = fogs[i] + "Merchancano"
    print(dogs)

main()
        '
