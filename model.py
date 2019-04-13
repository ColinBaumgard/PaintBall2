import player
import map


class Model:
    def __init__(self, map_size):

        # init player
        self.player = player.Player()

        # init map
        self.map = map.Map(map_size)



