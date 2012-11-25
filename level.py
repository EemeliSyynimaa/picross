# -*- coding: utf-8 -*-

from engine.graphics import scale_image
from engine.text import Label

import tile

class Level(object):
    """ This class holds the grid of the game. """

    def __init__(self, campaign, lvl_num, res, x=0, y=0, 
                 max_width=0, max_height=0, batch=None):
        self.path = "levels\\" + campaign + "\\" + str(lvl_num) + ".dat"
        self.res = res
        self.tile_size = 0
        self.x = x
        self.y = y
        self.max_width = max_width
        self.max_height = max_height
        self.batch = batch
        
        self.goal_grid = []
        self.play_grid = []
        self.row_numbers = []
        self.col_numbers = []
        self.row_labels = []
        self.col_labels = []
        self.tiles = []
        
        self.init_resources()
        self.init_goal_grid()
        self.init_play_grid()
        self.init_tile_size()
        self.init_position()
        self.init_tiles()
        self.init_row_numbers()
        self.init_col_numbers()
        self.init_row_labels()
        self.init_col_labels()
        
    def init_resources(self):
        self.res.load_image('tile_painted.png')
        self.res.load_image('tile_empty.png')
        self.res.load_image('tile_marked.png')
        self.res.load_image('tile_mistake.png')
        
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

        
    def init_tile_size(self):
        self.width = len(self.play_grid[0])
        self.height = len(self.play_grid)
        
        tile_w = self.max_width/self.width
        tile_h = self.max_height/self.height
        
        if tile_w > tile_h:
            self.tile_size = tile_h
        else:
            self.tile_size = tile_w
            
        self.res.gfx["tile_painted"] = scale_image(self.res.gfx["tile_painted"], 
                                                   self.tile_size, 
                                                   self.tile_size)
        
        self.res.gfx["tile_marked"] = scale_image(self.res.gfx["tile_marked"], 
                                                  self.tile_size, 
                                                  self.tile_size)
                
        self.res.gfx["tile_empty"] = scale_image(self.res.gfx["tile_empty"], 
                                                 self.tile_size, 
                                                 self.tile_size)
        
        self.res.gfx["tile_mistake"] = scale_image(self.res.gfx["tile_mistake"], 
                                                   self.tile_size, 
                                                   self.tile_size)
        
    def init_position(self):
        # First lets count the grid size
        self.width_in_pixels = self.width * self.tile_size
        self.height_in_pixels = self.height * self.tile_size
        # Then add the numeric instructions
        self.col_labels_in_pixels = self.height/2 * self.tile_size
        self.row_labels_in_pixels = self.width/2 * self.tile_size

        self.x = self.x - (self.width_in_pixels - self.row_labels_in_pixels) / 2
        self.y = self.y + (self.height_in_pixels - self.col_labels_in_pixels) / 2
    
    def init_tiles(self):
        blit_y = self.y - self.tile_size
        for y in range(0, self.height):
            blit_x = self.x
            
            for x in range(0, self.width):
                temp_tile = tile.Tile(self.res.gfx["tile_empty"])
                temp_tile.x = blit_x
                temp_tile.y = blit_y
                temp_tile.batch = self.batch
                
                self.tiles.append(temp_tile)
                    
                blit_x = blit_x + self.tile_size
                    
            blit_y = blit_y - self.tile_size
    
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
                             anchor_x='right', anchor_y='center',
                             batch=self.batch)
                
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
                             anchor_x='center', anchor_y='bottom',
                             batch=self.batch)
                
                new_line.append(temp)
                
                temp_y += self.tile_size
            
            self.col_labels.append(new_line)
            temp_x += self.tile_size
    
    def paint_tile(self, x, y):
        if self.is_mouse_on_grid(x, y):
            if self.is_tile_type(x, y, '#'):
                self.change_tile_value(x, y, '#')
            else:
                self.change_tile_value(x, y, 'E')
            
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
        temp_y = (self.y - y) / self.tile_size
        temp_x = (x - self.x) / self.tile_size
        
        temp_id = temp_y * self.width
        temp_id = temp_id + temp_x
        
        temp_img = None
        
        if value == '#':
            temp_img = self.res.gfx["tile_painted"]
        elif value == '-':
            temp_img = self.res.gfx["tile_empty"]
        elif value == 'X':
            temp_img = self.res.gfx["tile_marked"]
        elif value == 'E':
            temp_img = self.res.gfx["tile_mistake"]

        self.tiles[temp_id].image = temp_img
        
    def is_tile_type(self, x, y, value):
        
        return_value = False
        temp_y = self.y - y
        temp_x = x - self.x
        
        if self.goal_grid[temp_y/self.tile_size][temp_x/self.tile_size] == value:
            return_value = True
        
        return return_value
        
    def check_victory_conditions(self):
        conditions_met = True
        for y in range(0, len(self.goal_grid)):
            for x in range(0, len(self.goal_grid[y])):
                if self.goal_grid[y][x] == '#' and not \
                self.play_grid[y][x] == '#':
                    conditions_met = False
                    break
                    
        return conditions_met
        