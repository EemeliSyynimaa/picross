import grid

from engine import scene

class Game(scene.Scene):
    """ The class that makes the game go on. """

    def __init__(self, manager, path):
        super(Game, self).__init__(manager)
        
        self.grid = grid.Grid(path)
        self.init_resources()
        
    def init_resources(self):
        self.resource_manager.load_image("tile_down.png")
        self.resource_manager.load_image("tile_up.png")
   
    def on_draw(self):
        self.batch.draw()