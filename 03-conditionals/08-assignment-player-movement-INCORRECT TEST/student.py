# write your code here

def player_movement(position, left_arrow, right_arrow, shift):
    """
    left -> position - 1
    right -> position + 1

    """
    cached_positon = position
    position_ = position

    if left_arrow and not shift:
        position_ -= 1
    elif left_arrow and shift:
        position_ -= 2
    elif right_arrow and not shift:
        position_ += 1
    elif right_arrow and shift:
        position_ += 2
    elif left_arrow and right_arrow and shift:
        position_ = cached_positon
    return position_



