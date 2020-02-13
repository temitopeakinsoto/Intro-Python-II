# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_room):
        self.player_room  = player_room
    
    def __str__(self):
        return f"player in room {self.player_room}"


player = Player("Lagos Room")
print(player)

