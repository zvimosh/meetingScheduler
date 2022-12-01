## imports
import re

def getScheuldes():
    # Get the schedules from file
    # Return the schedules
    try:
        with open('schedules.txt') as f:
            schedules = f.readlines()
    except FileNotFoundError:
        print('ERROR: File not found')
        exit(1)
    return schedules

def parseSchedules(schedules):
    # Parse the schedules
    # Return the parsed schedules
    parsedSchedules = []
    for schedule in schedules:
        temp = schedule.split()
        for i in temp:
            nameSearch = re.match("^.*:$", i)
            daySearch = re.search("^!?()$", i)
            if nameSearch is not None:
                name = nameSearch.group(0)[:-1]
                print(name)
            else:
                print("Damn")
        
        print("")
    return parsedSchedules

if __name__ == '__main__':
    schedules = getScheuldes()
    parsedSchedules = parseSchedules(schedules)
    #print(schedules)
    #print(parsedSchedules)

