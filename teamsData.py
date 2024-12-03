import random
data = open("data.txt", "a")
data.write("\nStart of new data")

names = ["Benjamin", "Ashton", "Darin", "Jack"]
preference = ["Ashton", "Benjamin", "Jack", "Darin"]
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
#teams = 2

# Makes sure that no specific spot in the list is more advantageous by changing the advantageous spots
bump = random.randint(0, len(names))


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

#nums = [1, 2, 3, 4]
#bump = 4
#print("Start nums: " + str(nums))
#print("Bump: " + str(bump))
for i in range(len(preference)):
    t = i + bump
    if t >= len(preference): 
        t -= len(preference)
    if not preference[t] == "none":
        try: 
            targetIndex = names.index(preference[t])
        except:
            print("Error checking preference. This is likely caused by a spelling error in a preference or name.")
        try:
            if not nums[targetIndex + 1] in static:
                #print("Add")
                #print(t)
                #print(targetIndex)
                nums.insert(targetIndex + 1, nums[t])
                #print("Insert " + str(nums))
                if t > targetIndex + 1: nums.pop(t + 1)
                else: nums.pop(t)
                #print("Delete " + str(nums))
                nums.insert(t, nums[targetIndex + 1])
                #print("Insert " + str(nums))
                nums.pop(targetIndex + 2)
                #print("Delete " + str(nums))
                static.append(nums[targetIndex])
                static.append(nums[t])
            elif (not nums[targetIndex - 1] in static) and (not targetIndex - 1 == -1):
                #print("Subtract")
                #print(t)
                #print(targetIndex)
                nums.insert(targetIndex - 1, nums[t])
                #print("Insert " + str(nums))
                if t > targetIndex - 1: nums.pop(t + 1)
                else: nums.pop(t)
                #print("Delete " + str(nums))
                nums.insert(t, nums[targetIndex - 1])
                #print("Insert " + str(nums))
                nums.pop(targetIndex - 1)
                #print("Delete " + str(nums))
                static.append(nums[targetIndex])
                static.append(nums[t])
        except: 
            if (not nums[targetIndex - 1] in static) and (not targetIndex - 1 == -1):
                #print("Subtract")
                #print(t)
                #print(targetIndex)
                nums.insert(targetIndex - 1, nums[t])
                #print("Insert " + str(nums))
                if t > targetIndex - 1: nums.pop(t + 1)
                else: nums.pop(t)
                #print("Delete " + str(nums))
                nums.insert(t, nums[targetIndex - 1])
                #print("Insert " + str(nums))
                nums.pop(targetIndex - 1)
                #print("Delete " + str(nums))
                static.append(nums[targetIndex])
                static.append(nums[t])
#print(nums)       

for i in range(teams):
    result = "Team " + str(i + 1) + ": "
    for x in nums:
        if x <= split * (i + 1) and x > split * i:
            result += names[nums.index(x)] + " "
    print(result)
data.write("\n")
data.close()