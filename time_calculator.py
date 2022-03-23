def add_time(start, duration, weekday=""):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    minstart = int(start.split(":")[1].split(" ")[0])
    if start.split(" ")[1] == "PM":
        hstart = int(start.split(":")[0]) + 12
    else:
        hstart = int(start.split(":")[0])

    hadd = int(duration.split(":")[0])
    minadd = int(duration.split(":")[1])

    hf = hstart + hadd
    minf = minstart + minadd
    alternate = False
    if minf > 59:
        hf += 1
        minf -= 60
        if hf == 12:
            alternate = True

    days = 0
    while hf >= 24 :
        days += 1
        hf -= 24

    pm = False
    if hf > 12:
        hf -= 12
        pm = True
    if alternate == True:
        pm = not pm
    if hf == 0:
        hf = 12    

    time = ""
    time += str(hf) + ":" + str(minf).zfill(2) + " "
    if pm:
        time += "PM"
    else:  
        time += "AM"
    
    if weekday != "":
        dayf = weekdays[((weekdays.index(weekday.title()) + (days % 7)) % 7)]
        time += ", " + dayf
    
    if days == 1:
        time += " (next day)"
    if days > 1:
        time += " (" + str(days) + " days later)"
        
    return(time)