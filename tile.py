from engine import sprite

class Tile(sprite.Sprite):
    """ A tile class! """

    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(*args, **kwargs)
        