from sys import argv

process, sensePath, antisensePath = argv

senseData = open(sensePath)
antisenseData = open(antisensePath)
antisenseLines = antisenseData.readlines()

def getStart(line):
    d = line.split()
    return int(d[2])

def getEnd(line):
    d = line.split()
    return int(d[3])

# Function to find lines in the antisense data set who's start point is between
# 5 and 30 base pairs 3' from the start of the given sense line
def getNearbyAntisenseLines(senseLine):
    senseEnd = getEnd(senseLine)
    outputLines = []
    for antisenseLine in antisenseLines:
        asenseStart = getStart(antisenseLine)
        distance = asenseStart - senseEnd 
        if distance > 5 and distance < 30:
            outputLines.append(antisenseLine)
    return outputLines


def main():
    for line in senseData.readlines():
        nearbyLines = getNearbyAntisenseLines(line)
        # if antisense start - sense end > 5 & < 30

        for aLine in nearbyLines:
            print line
            print aLine
            print '\n'


if __name__ == '__main__':
    main()