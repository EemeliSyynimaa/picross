# -*- coding: utf-8 -*-

import level

from engine import scene
from pyglet.window import mouse

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager, campaign, lvl_num, 
                 screen_width, screen_height):
        super(Game, self).__init__(manager)
        
        self.campaign = campaign
        self.lvl_num = lvl_num
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.init_level()
        self.init_resources()
        
    def init_resources(self):
        pass
    
    def init_level(self):
        
        self.init_level_size()
        self.level = level.Level(self.campaign, self.lvl_num, self.res, 
                                 self.screen_width/2, self.screen_height/2,
                                 self.level_size, self.level_size)
                
    
    def init_level_size(self):
        self.level_size = self.screen_width
        
        if self.screen_width > self.screen_height:
            self.level_size = self.screen_height
        
        # 0.90 so it doesnt take the whole screen.
        # And 30 % for numeric instructions.
        self.level_size = int(self.level_size * 0.95 * 0.70)
    
    def update(self, dt):
        if self.level.check_victory_conditions():
            self.manager.activate_scene("game_won", self.campaign, 
                                        self.lvl_num, self.screen_width,
                                        self.screen_height)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.level.paint_tile(x, y)
        elif button == mouse.RIGHT:
            self.level.mark_tile(x, y)
        elif button == mouse.MIDDLE:
            self.level.clear_tile(x, y)
            
    def on_draw(self):
        self.batch.draw()
        self.level.draw()