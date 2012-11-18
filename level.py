class Level(object):
    """ This class holds the grid of the game. """

    def __init__(self, path, resource_manager, x=0, y=0):
        self.path = path
        self.resource_manager = resource_manager
        self.goal_grid = []
        self.play_grid = []
        self.tile_size = 32
        self.x = x
        self.y = y
        
        self.init_resources()
        self.init_goal_grid()
        self.init_play_grid()
        self.init_position()
        
    def init_resources(self):
        self.resource_manager.load_image('tile_painted.png')
        self.resource_manager.load_image('tile_empty.png')
        
    def init_goal_grid(self):
        try:
            data_file = open(self.path + ".dat", 'r')
            
            line = data_file.readline()
            
            while line:
                self.parse_line(line)
                line = data_file.readline() 

        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
        else:
            data_file.close()
            
    def parse_line(self, line):
        new_line = []
        
        for char in line:
            if char != '\n':
                new_line.append(char)
                
        self.goal_grid.append(new_line)
            
    def init_play_grid(self):
        for y in self.goal_grid:
            new_line = []
            for x in y:
                new_line.append('-')
                
            self.play_grid.append(new_line)
        
    def init_position(self):
        self.width = len(self.play_grid[0])
        self.height = len(self.play_grid)
        self.width_in_pixels = self.width * self.tile_size
        self.height_in_pixels = self.height * self.tile_size
        
        self.x = self.x - self.width_in_pixels / 2
        self.y = self.y + self.height_in_pixels / 2

    def reset(self):
        pass
            
    def draw(self):
        for y in range(0, len(self.goal_grid)):
            for x in range(0, len(self.goal_grid[y])):
                blit_x = self.x + x * self.tile_size
                blit_y = self.y - y * self.tile_size - self.tile_size
                
                if self.goal_grid[y][x] == "#":
                    self.resource_manager.gfx['tile_painted'].blit(blit_x, blit_y)
                else:
                    self.resource_manager.gfx['tile_empty'].blit(blit_x, blit_y )
    
        