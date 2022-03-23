def add_time(startTime, duration, weekday=""):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    minStart = int(startTime.split(":")[1].split(" ")[0])
    if startTime.split(" ")[1] == "PM":
        hourStart = int(startTime.split(":")[0]) + 12
    else:
        hourStart = int(startTime.split(":")[0])

    addHours = int(duration.split(":")[0])
    addMins = int(duration.split(":")[1])

    hourSum = hourStart + addHours
    minSum = minStart + addMins
    alternate = False
    if minSum > 59:
        hourSum += 1
        minSum -= 60
        if hourSum == 12:
            alternate = True

    days = 0
    while hourSum >= 24 :
        days += 1
        hourSum -= 24

    pm = False
    if hourSum > 12:
        hourSum -= 12
        pm = True
    if alternate == True:
        pm = not pm
    if hourSum == 0:
        hourSum = 12    

    finalTIme = ""
    finalTIme += str(hourSum) + ":" + str(minSum).zfill(2) + " "
    if pm:
        finalTIme += "PM"
    else:  
        finalTIme += "AM"
    
    if weekday != "":
        dayf = weekdays[((weekdays.index(weekday.title()) + (days % 7)) % 7)]
        finalTIme += ", " + dayf
    
    if days == 1:
        finalTIme += " (next day)"
    if days > 1:
        finalTIme += " (" + str(days) + " days later)"
        
    return(finalTIme)