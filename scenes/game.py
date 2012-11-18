# -*- coding: utf-8 -*-

import level

from engine import scene
from pyglet.window import mouse

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager, campaign, lvl_num, 
                 screen_width, screen_height):
        super(Game, self).__init__(manager)
        
        self.level = level.Level(campaign, lvl_num, self.gfx, 
                                 screen_width/2, screen_height/2)
        self.init_resources()
        
        self.campaign = campaign
        self.lvl_num = lvl_num
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def init_resources(self):
        pass
    
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