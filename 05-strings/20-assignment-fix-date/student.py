# write your code here

def fix_date(date: str):
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]

    return "".join(year + "/" + month + "/" + day)