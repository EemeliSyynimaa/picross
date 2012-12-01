# -*- coding: utf-8 -*-

import level

from engine import scene
from engine.graphics import scale_image
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
        
        self.resize_background()
        
    def init_resources(self):
        self.res.load_image("background.png", "levels\\"+self.campaign)
    
    def init_level(self):
        
        self.init_level_size()
        self.level = level.Level(self.campaign, self.lvl_num, self.res, 
                                 self.screen_width/2, self.screen_height/2,
                                 self.level_size, self.level_size,
                                 self.batch)
    
    def init_level_size(self):
        self.level_size = self.screen_width
        
        if self.screen_width > self.screen_height:
            self.level_size = self.screen_height
        
        # 0.95 so it doesnt take the whole screen.
        # And 30 % for numeric instructions.
        self.level_size = int(self.level_size * 0.95 * 0.70)
    
    def resize_background(self):
        width = float(self.screen_width) / float(self.res.gfx['background'].width)
        height = float(self.screen_height) / float(self.res.gfx['background'].height)
        
        if width > height:
            height = width * self.res.gfx['background'].height
            width = width * self.res.gfx['background'].width
        else:
            width = height * self.res.gfx['background'].width
            height = height * self.res.gfx['background'].height
            
        self.res.gfx['background'] = scale_image(self.res.gfx['background'],
                                                 width,
                                                 height)
        
        self.res.gfx['background'].anchor_x = self.res.gfx['background'].width/2
        self.res.gfx['background'].anchor_y = self.res.gfx['background'].height/2
        
        print(self.res.gfx['background'].width)
        print(self.res.gfx['background'].height)
    
    def update(self, dt):
        if self.level.check_victory_conditions():
            self.manager.activate_scene('game_won', self.campaign, 
                                        self.lvl_num, self.screen_width,
                                        self.screen_height)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.level.paint_tile(x, y)
        elif button == mouse.RIGHT:
            self.level.mark_tile(x, y)
            
    def on_draw(self):
        self.res.gfx['background'].blit(self.screen_width/2,
                                        self.screen_height/2)
        self.batch.draw()
