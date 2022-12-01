## imports
import re
import json

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
    parsedSchedules = {}
    for line in schedules:
        schedule = line.split()
        name = schedule[0][:-1]
        day =  (re.search("(sunday|monday|tuesday|wednesday|thursday|friday|saturday)",line, flags=re.IGNORECASE)).group(0)
        time = (re.search("\d{2}:\d{2}",line)).group(0)
        if "yard" in schedule:
            location = "yard"
        else:  
            location = "" 
        #print(line)    
        print('"Name":"{0}", "Location"":"{1}", "Day":"{2}", "time":"{3}"'.format(name,location,day,time))
        parsedSchedules.append('Name:{0}, Location:{1}, Day:{2}, time:{3}'.format(name,location,day,time))

        #jsonObj = json.dumps(list)
        #print(jsonObj)
    ## need to work on serilizating to json or format that can work with
    print(parsedSchedules)
    jsonObj = json.dumps(parsedSchedules)
    print(jsonObj)


    return parsedSchedules

if __name__ == '__main__':
    schedules = getScheuldes()
    parsedSchedules = parseSchedules(schedules)
    #print(schedules)
    #print(parsedSchedules)

