from engine import scene

import level

class Game(scene.Scene):
    """ The class that makes the game go on. """

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        
        self.level = level.Level()
        