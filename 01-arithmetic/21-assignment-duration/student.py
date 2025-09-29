# write your code here

def hours(duration):
    return duration // 3600

def minutes(duration):
    h = hours(duration)
    duration -= h * 3600
    return duration // 60

def seconds(duration):
    h = hours(duration)
    duration -= (h * 3600)
    m = minutes(duration)
    duration -= (m * 60)
    return duration # nr of seconds left