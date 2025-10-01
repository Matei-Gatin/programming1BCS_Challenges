# write your code here
def next_player(player, player_count):
    player_diff = player_count - player
    if player_diff <= 1:
        return 0
    return player + 1


print(next_player(9, 10))