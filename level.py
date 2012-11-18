# -*- coding: utf-8 -*-

from engine.text import Label

class Level(object):
    """ This class holds the grid of the game. """

    def __init__(self, campaign, lvl_num, res, x=0, y=0):
        self.path = "levels\\" + campaign + "\\" + str(lvl_num) + ".dat"
        self.res = res
        self.tile_size = 32
        self.x = x
        self.y = y
        
        self.goal_grid = []
        self.play_grid = []
        self.row_numbers = []
        self.col_numbers = []
        self.row_labels = []
        self.col_labels = []

        
        self.init_resources()
        self.init_goal_grid()
        self.init_play_grid()
        self.init_position()
        self.init_row_numbers()
        self.init_col_numbers()
        self.init_row_labels()
        self.init_col_labels()
        
    def init_resources(self):
        self.res.load_image('tile_painted.png')
        self.res.load_image('tile_empty.png')
        self.res.load_image('tile_marked.png')
        
    def init_goal_grid(self):
        try:
            data_file = open(self.path, 'r')
            
            line = data_file.readline()
            
            while line:
                self.parse_line(line)
                line = data_file.readline() 

        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            print(self.path)
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
            
    def init_row_numbers(self):
        for row in self.goal_grid:
            new_line = []
            consecutive_tiles = 0
            for tile in row:
                if tile == '#':
                    consecutive_tiles += 1
                else:
                    if consecutive_tiles:
                        new_line.append(consecutive_tiles)
                        consecutive_tiles = 0
                        
            if consecutive_tiles:
                new_line.append(consecutive_tiles)
            
            self.row_numbers.append(new_line)
        
    def init_col_numbers(self):
        consecutive_tiles = []
        for col in self.goal_grid[0]:
                new_line = []
                consecutive_tiles.append(0)
                self.col_numbers.append(new_line)
            
        for row in self.goal_grid:
            for tile in range(0, len(row)):
                if row[tile] == '#':
                    consecutive_tiles[tile] += 1
                else:
                    if consecutive_tiles[tile]:
                        self.col_numbers[tile].append(consecutive_tiles[tile])
                        consecutive_tiles[tile] = 0
        
        for i in range(0, len(consecutive_tiles)):
            if consecutive_tiles[i]:
                self.col_numbers[i].append(consecutive_tiles[i])
                
    def init_position(self):
        self.width = len(self.play_grid[0])
        self.height = len(self.play_grid)
        self.width_in_pixels = self.width * self.tile_size
        self.height_in_pixels = self.height * self.tile_size
        
        self.x = self.x - self.width_in_pixels / 2
        self.y = self.y + self.height_in_pixels / 2
        
    def init_row_labels(self):
        temp_y = self.y - self.tile_size/2
        for row in self.row_numbers:
            new_line = []
            temp_x = self.x - self.tile_size/2
            
            for line in reversed(row):
                temp = Label(str(line), 
                             font_name='Verdana',
                             font_size=self.tile_size/2,
                             x=temp_x, y=temp_y,
                             anchor_x='right', anchor_y='center')
                
                new_line.append(temp)
                
                temp_x -= self.tile_size
                
            self.row_labels.append(new_line)
            temp_y -= self.tile_size
    
    def init_col_labels(self):
        temp_x = self.x + self.tile_size/2
        for col in self.col_numbers:
            new_line = []
            temp_y = self.y + self.tile_size/2
            
            for line in reversed(col):
                temp = Label(str(line),
                             font_name='Verdana',
                             font_size=self.tile_size/2,
                             x=temp_x, y=temp_y,
                             anchor_x='center', anchor_y='bottom')
                
                new_line.append(temp)
                
                temp_y += self.tile_size
            
            self.col_labels.append(new_line)
            temp_x += self.tile_size

    def reset(self):
        pass
    
    def paint_tile(self, x, y):
        if self.is_mouse_on_grid(x, y):
            self.change_tile_value(x, y, '#')
            
    def mark_tile(self, x, y):
        if self.is_mouse_on_grid(x, y):
            self.change_tile_value(x, y, 'X')
            
    def clear_tile(self, x, y):
        if self.is_mouse_on_grid(x, y):
            self.change_tile_value(x, y, '-')
            
    def is_mouse_on_grid(self, x, y):
        return_value = False
        
        if x > self.x and x < self.x + self.width_in_pixels and \
        y < self.y and y > self.y - self.height_in_pixels:
            return_value = True
            
        return return_value
                
    def change_tile_value(self, x, y, value):
        temp_y = self.y - y
        temp_x = x - self.x

        self.play_grid[temp_y/32][temp_x/32] = value
        
    def check_victory_conditions(self):
        conditions_met = True
        for y in range(0, len(self.goal_grid)):
            for x in range(0, len(self.goal_grid[y])):
                if self.goal_grid[y][x] == '#' and not \
                self.play_grid[y][x] == '#':
                    conditions_met = False
                    break
                    
        return conditions_met
            
    def draw(self):
        self.draw_play_grid()
        self.draw_row_labels()
        self.draw_col_labels()
        
    def draw_row_labels(self):
        for row in self.row_labels:
            for label in row:
                label.draw()
                
    def draw_col_labels(self):
        for col in self.col_labels:
            for label in col:
                label.draw()
        
    def draw_play_grid(self):
        for y in range(0, len(self.play_grid)):
            for x in range(0, len(self.play_grid[y])):
                blit_x = self.x + x * self.tile_size
                blit_y = self.y - y * self.tile_size - self.tile_size
                
                if self.play_grid[y][x] == "#":
                    self.res.gfx["tile_painted"].blit(blit_x, blit_y)
                elif self.play_grid[y][x] == '-':
                    self.res.gfx["tile_empty"].blit(blit_x, blit_y )
                elif self.play_grid[y][x] == 'X':
                    self.res.gfx["tile_marked"].blit(blit_x, blit_y )
        