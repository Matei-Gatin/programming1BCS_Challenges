# write your code here

def parse_day(string):
    return int(string[0:2])

def parse_month(string):
    return int(string[3:5])

def parse_year(string):
    return int(string[6:10])

print(parse_day('10/02/2000'))
print(parse_month('10/02/2000'))
print(parse_year('10/20/0200'))