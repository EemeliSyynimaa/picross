class Grid(object):
    """ This class holds the grid of the game. """

    def __init__(self, path, resource_manager):
        self.path = path
        self.resource_manager = resource_manager
        self.original_data = []
        self.play_data = []
        self.tile_size = 32
        
        self.init_resources()
        self.init_original_data()
        self.init_play_data()
        self.init_position()
        
    def init_resources(self):
        self.resource_manager.load_image('tile_painted.png')
        self.resource_manager.load_image('tile_empty.png')
        
    def init_original_data(self):
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
                
        self.original_data.append(new_line)
            
    def init_play_data(self):
        for y in self.original_data:
            new_line = []
            for x in y:
                new_line.append('-')
                
            self.play_data.append(new_line)
        
    def init_position(self):
        self.width = len(self.original_data[0])
        self.height = len(self.original_data)
        self.width_in_pixels = self.width * self.tile_size
        self.height_in_pixels = self.height * self.tile_size
        
        self.x = 640 - self.width_in_pixels / 2
        self.y = 360 + self.height_in_pixels / 2

    def reset(self):
        pass
            
    def draw(self):
        for y in range(0, len(self.original_data)):
            for x in range(0, len(self.original_data[y])):
                blit_x = self.x + x * self.tile_size
                blit_y = self.y - y * self.tile_size - self.tile_size
                
                if self.original_data[y][x] == "#":
                    self.resource_manager.gfx['tile_painted'].blit(blit_x, blit_y)
                else:
                    self.resource_manager.gfx['tile_empty'].blit(blit_x, blit_y )
    
        