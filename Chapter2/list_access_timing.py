import datetime
import random
import time


def main():
    f = open("ListAccessTiming.xml", 'w')
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')

    f.write('<Plot title="Average List Element Access Time">\n')

    # test lists of size 1000 to 200000
    xmin = 1000
    xmax = 200000

    # record the list sizes in xList and the average access time within
    # a list that size in yList for 1000 retrievals
    xList = []
    yList = []

    for x in range(xmin, xmax + 1, 1000):
        xList.append(x)
        prod = 0

        # creates a list of size x with all 0's
        lst = [0] * x

        # let garbage collection/memory allocation complete or settle down
        time.sleep(1)

        # time before the 1000 test retrievals
        starttime = datetime.datetime.now()

        for v in range(1000):
            index = random.randint(0, x - 1)
            val = lst[index]
            prod = prod * val
        endtime = datetime.datetime.now()

        deltaT = endtime - starttime

        # divide by 1000 for avg, multipy by 1000000 for microseconds
        accessTime = deltaT.total_seconds() * 1000

        yList.append(accessTime)

    f.write('  <Axes>\n')
    f.write('    <XAxis min="%s" max="%s">List Size</XAxis>\n' % (str(xmin), str(xmax)))
    f.write('    <YAxis min="%i" max="60">Microseconds</YAxis>\n' % min(yList))
    f.write('  </Axes>\n')

    f.write('  <Sequence title="Average Access Time vs List Size" color="red">\n')

    for i in range(len(xList)):
        f.write('    <DataPoint x="%i" y="%i"/>\n' % (xList[i], yList[i]))

    f.write('  </Sequence>\n')

    # tests access at 100 random locations within a list of 200000 elements to see that all the locations
    #   can be access in about the same amount of time
    xList = lst
    yList = [0] * 200000

    time.sleep(2)

    for i in range(100):
        starttime = datetime.datetime.now()
        i = random.randint(0, 200000 - 1)
        xList[i] = xList[i] + 1
        endtime = datetime.datetime.now()
        deltaT = endtime - starttime
        yList[i] = yList[i] + deltaT.total_seconds() * 1000000

    f.write('  <Sequence title="Access Time Distribution" color="blue">\n')

    for i in range(len(xList)):
        if xList[i] > 0:
            f.write('    <DataPoint x="%i" y="%s"/>\n' % (i, str(yList[i] / xList[i])))

    f.write('  </Sequence>\n')
    f.write('</Plot>\n')
    f.close()


if __name__ == '__main__':
    main()
