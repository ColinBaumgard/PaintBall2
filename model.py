import player
import map


class Model:
    def __init__(self, map_size, level):

        # init player
        self.player = player.Player(coords=(map_size[0]/2, 50, 0))

        # init map
        self.map = map.Map(map_size, level)



