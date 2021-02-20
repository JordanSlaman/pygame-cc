class Item:

    def interact(self, tile, player):
        raise NotImplementedError

    @property
    def sprite(self):
        raise NotImplementedError
