class Grid(object):
    """ This class holds the grid of the game. """

    def __init__(self, path, resource_manager):
        self.x = 0
        self.y = 0
        self.path = path
        self.resource_manager = resource_manager
        
        self.init_resources()
        
    def init_resources(self):
        self.resource_manager.load_image("tile_down.png")
        self.resource_manager.load_image("tile_up.png")
    
    def draw(self):
        self.resource_manager.gfx["tile_down"].blit(0, 0)
    
        