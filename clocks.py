clocks = [300, 308, 357, 360, 420, 480, 485, 540]

# Correct answer: 5:00, 5:08, 5:57, 6:00, 7:00, 8:00, 8:05, 9:00

def verify():
    converted_times = []
    for clock in clocks:
        converted_times.append(str(clock // 60) + ":" + str(clock % 60).zfill(2))
    print("Converted times:", converted_times)
    # All times are unique
    checked_times = []
    for clock in clocks:
        if clock in checked_times:
            return False
        checked_times.append(clock)
    print("Unique check passed")
    # 5 clocks must be on the hour
    count = 0
    for clock in clocks:
        if clock % 60 == 0:
            count += 1
    if count != 5:
        return False
    print("On the hour check passed")
    # Clock #4's neighbors must contain a 7
    if "7" not in converted_times[2] or "7" not in converted_times[4]:
        return False
    print("Clock #4 neighbor check passed")
    # None should be set to times that contain the number 1, 2, 3, or 4
    for time in converted_times:
        if "1" in time or "2" in time or "3" in time or "4" in time:
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
        return False
    print("Clock #7 reverse check passed")
    return True
        

print(verify())