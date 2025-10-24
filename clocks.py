clocks = [0, 0, 0, 0, 0, 0, 0, 0]

def verify():
    # All times are unique
    checked_times = []
    for clock in clocks:
        if clock in checked_times:
            print("Unique check failed!")
            return False
        checked_times.append(clock)
    print("Unique check passed")
    # 5 clocks must be on the hour
    count = 0
    for clock in clocks:
        if clock % 60 == 0:
            count += 1
    if count != 5:
        print("On the hour check failed!")
        return False
    print("On the hour check passed")
    # Clock #4's neighbors must contain a 7
    if "7" not in converted_times[2] or "7" not in converted_times[4]:
        print("Clock #4 neighbor check failed!")
        return False
    print("Clock #4 neighbor check passed")
    # None should be set to times that contain the number 1, 2, 3, or 4
    for time in converted_times:
        if "1" in time or "2" in time or "3" in time or "4" in time:
            print("No 1, 2, 3, or 4 check failed!")
            return False
    print("No 1, 2, 3, or 4 check passed")
    # Clock #7 should be set to a time that contains the same three numbers of another clock here but in reverse order
    target_time = converted_times[6].replace(":", "")
    i = 0
    while i < len(converted_times):
        time = converted_times[i].replace(":", "")[::-1]
        if i != 6 and time == target_time:
            break
        i += 1
    else:
        print("Clock #7 reverse check failed")
        return False
    print("Clock #7 reverse check passed")
    # All times must be in ascending order
    if clocks == sorted(clocks):
        print("Ascending order check failed!")
        return False
    print("Ascending order check passed")
    return True
        
while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    converted_times = []
    for clock in clocks:
        if clock // 60 == 0:
            clock += 720
        converted_times.append(str(clock // 60) + ":" + str(clock % 60).zfill(2))
    print("Current times:", converted_times)
    ans = input("Select an action:\n\
                Read the \033[4mrules\033[0m\n\
                Change a \033[4mclock\033[0m\n\
                \033[4mCheck\033[0m your answer\n")
    ans = ans.lower()
    match ans:
        case "rules":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            input("The Rules:\n\
                  1. All times must be unique\n\
                  2. 5 clocks must be on the hour (ending in :00)\n\
                  3. Clock #4's neighbors must both contain a 7\n\
                  4. No clocks can contain 1, 2, 3, or 4\n\
                  5. Clock #7 must be set to a time that contains the same three numbers of another clock, but in reverse order\n\
                  6. All times must be in ascending order\n\
                  Press enter to continue...")
        case "clock":
            clock_number = input("Which clock would you like to change? (1-8) ")
            try:
                clock_number = int(clock_number)
                if clock_number < 1 or clock_number > 8:
                    raise ValueError()
                new_value = input("What time do you want to set it to? (x:xx) ").split(":")
                if len(new_value) != 2:
                    raise ValueError()
                new_value[0] = int(new_value[0])
                new_value[1] = int(new_value[1])
                if new_value[0] < 1 or new_value[0] > 12 or new_value[1] < 0 or new_value[1] > 59:
                    raise ValueError()
                new_minutes = 0
                if new_value[0] == 12:
                    new_minutes = 0
                else:
                    new_minutes = new_value[0] * 60
                new_minutes += new_value[1]
                clocks[clock_number - 1] = new_minutes
            except:
                input("Invalid input.\nPress enter to continue...")
        case "check":
            result = verify()
            if result:
                break
            input("Press enter to continue...")

input("Congratulations, you have solved the puzzle! Your answer: " + str(converted_times) + "\nPress enter to continue...")