class Level(object):
    """ This class holds the level player is playing. """

    def __init__(self, level_file):
        self.x = 0
        self.y = 0
        self.width = 256
        self.height = 256
        self.file = level_file
    
    def on_draw(self):
        pass
    
        