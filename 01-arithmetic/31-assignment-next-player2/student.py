# write your code here

def next_player2(player, player_count):
    player_diff = player_count - player
    if player_diff <= 0:
        return player + 1
    return player + 1