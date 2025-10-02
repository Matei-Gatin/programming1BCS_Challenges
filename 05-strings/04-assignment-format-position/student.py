# write your code here
def format_position(x, y):
    return f"({x:.3f}, {y:.3f})"

print(format_position(1.23456, 2.34567))  # should return "(1.235, 2.34567)"
print(format_position(1.2, 3.4567))        # should return "(1.2, 3.4567)"
print(format_position(1.0, 2.0))          # should return "(1.0, 2.0)"