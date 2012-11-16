import grid

from engine import scene

class Game(scene.Scene):
    """ The class that makes the game go on. """

    def __init__(self, manager, path):
        super(Game, self).__init__(manager)
        
        self.grid = grid.Grid(path, self.resource_manager)
        self.init_resources()
        
    def init_resources(self):
        pass
   
    def on_draw(self):
        self.batch.draw()
        self.grid.draw()