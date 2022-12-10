## imports
import re
import json

def find_value_by_key(key, value, list_of_dicts):
    """Return True if value is found in list_of_dicts, False otherwise"""

    #print(f"key: {key}, value: {value}, list_of_dicts: {list_of_dicts}")
    if any(_dict[key] == value for _dict in list_of_dicts if key in _dict):
        return True
    else:
        return False

def getScheuldes():
    # Get the schedules from file
    # Return the schedules
    try:
        with open('schedules1.txt') as f:
            schedules = f.readlines()
    except FileNotFoundError as e:
        print('ERROR:', e)
        exit(1)
    return schedules

def parseSchedules(schedules):
    # Parse the schedules
    # Return the parsed schedules
    parsedSchedules = []
    schedulesJson = {}
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
        dict_full = {'name':name, 'location':location, 'day':day, 'time':time}
        dict = {'location':location, 'day':day, 'time':time}
        #print('"Name":"{0}", "Location"":"{1}", "Day":"{2}", "time":"{3}"'.format(name,location,day,time))
        parsedSchedules.append(dict_full)
        if not schedulesJson:
            schedulesJson[name] = [dict]
        elif name in schedulesJson:
            schedulesJson[name].append(dict)
        else:
            schedulesJson.update({name:[dict]})


    #print(schedulesJson)
    return schedulesJson

if __name__ == '__main__':
    student = []
    parsedSchedules = parseSchedules(schedules = getScheuldes())
    
    #print(parsedSchedules)
    
"""     for item in parsedSchedules:
        if find_value_by_key(key = 'name', value = item['name'], list_of_dicts = parsedSchedules):
            student.append(item)
        else:
            student.append(item) """
    #print(student)



