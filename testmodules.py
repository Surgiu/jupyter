def lineCount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count