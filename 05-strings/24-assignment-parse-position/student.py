# write your code here

def parse_position_x(string: str) -> float:
    split_string_pos_x = string.split(",")[0][1:]
    return float(split_string_pos_x)

def parse_position_y(string: str) -> float:
    split_string_pos_y = string.split(",")[1][:-1].strip()
    return float(split_string_pos_y)

parse_position_x("(12.453, 9.120)")
parse_position_y("(12.453, 9.120)")
