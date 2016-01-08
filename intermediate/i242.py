
def vhsRecord():
    bucket = [0] * 2400
    times = readFile()
    recorded = len(times)
    for ti in times:
        temp_bucket = bucket
        temp = True
        for i in range(int(ti[0]), int(ti[1])):
            if bucket[i] == 0:
                temp_bucket[i] = 1
            else:
                recorded -= 1
                temp = False
            if not temp:
                break
        if temp:
            bucket = temp_bucket
    return recorded


def readFile():
    text_file = open("i242.txt", "r")
    lines = text_file.read().splitlines()
    times, new_times = [], []

    for line in lines:
        times.append(line.split(','))
    for time in times:
        new_times.append(time[0].split(" "))
    return new_times
# print len(lines)

# print readFile()

print vhsRecord()