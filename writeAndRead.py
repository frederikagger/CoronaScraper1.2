def saveData(message):
    file = open('numberOfcases.txt', 'w')
    file.write(message)


def checkData():
    file = open('numberOfcases.txt', 'r')
    return int(file.read())


