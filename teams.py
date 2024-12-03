import random
names = ["Benjamin", "Ashton", "James", "Jack"]
preference = ["Ashton", "James", "Jack", "Benjamin"]
nums = []
static = []

while True:
    name = input("Give a name to add, or type exit to finish. ")
    if name == "exit":
        break
    else: 
        names.append(name)
        preference.append(input("Give the student's preferred partner, or type none for none. "))

while True:
    try:
        teams = int(input("How many teams? "))
    except:
        print("Must be a whole number.")
    else:
        break

# Makes sure that no specific spot in the list is more advantageous by changing the advantageous spots
bump = random.randint(1, len(names))


# If these aren't the same length, everything gets offset and breaks.
if (len(names) != len(preference)):
    print("\nPreferences & names are different lengths. Make sure any pre-existing names & preferences are properly inputted.")
    print("Names length: " + str(len(names)) + " Preferences length: " + str(len(preference)))
    print("Names: " + str(names))
    print("Preferences: " + str(preference) + "\n")
    input("Press enter to quit.")
    quit()

for i in range(len(names)):
    num = random.randint(1, len(names))
    # Make sure there are no duplicate numbers so the assigning works properly
    while num in nums:
        num += 1
        if num > len(names):
            num = 1
    nums.insert(i, num)
split = len(nums) / teams

for i in nums:
    pass

for i in range(teams):
    result = "Team " + str(i + 1) + ": "
    for x in nums:
        if x <= split * (i + 1) and x > split * i:
            result += names[nums.index(x)] + " "
    print(result)