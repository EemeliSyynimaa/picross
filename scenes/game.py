import level

from engine import scene

class Game(scene.Scene):
    """ The class that makes the game go on. """

    def __init__(self, manager, campaign, lvl_no):
        super(Game, self).__init__(manager)
        
        level.Level("campanjaaa")
        
        self.init_resources()
        
    def init_resources(self):
        self.resource_manager.load_image("tile_down.png")
        self.resource_manager.load_image("1.png", "levels//test.lvl")
        
    def on_draw(self):
        self.resource_manager.gfx["1"].blit(0,0)
        self.resource_manager.gfx["tile_down"].blit(100,100)
        self.batch.draw()