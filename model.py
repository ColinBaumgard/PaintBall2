import player
import map


class Model:
    def __init__(self):
        print('model')

        # init player
        self.player = player.Player()

        # init map
        self.map = map.Map()



