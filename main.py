#!/usr/bin/env python
# -*- coding: utf-8 -*-

from engine import engine
from scenes import game, game_won, game_lost
from scenes import menu_main, menu_campaign, menu_level

class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 720
        
        self.engine = engine.Engine(width=self.screen_w, 
                                    height=self.screen_h,
                                    fullscreen=False)
        
        self.init_resources()
        self.init_scenes()
        
        self.engine.run()
        
    def init_resources(self):
        self.engine.add_resource_path('gfx')
        
    def init_scenes(self):
        self.engine.scene_manager.add_scene('game', game.Game)
        self.engine.scene_manager.add_scene('game_won', game_won.GameWon)
        self.engine.scene_manager.add_scene('game_lost', game_lost.GameLost)
        self.engine.scene_manager.add_scene('menu_main', menu_main.MenuMain)
        self.engine.scene_manager.add_scene('menu_campaign', 
                                            menu_campaign.MenuCampaign)
        self.engine.scene_manager.add_scene('menu_level', 
                                            menu_level.MenuLevel)
        self.engine.scene_manager.activate_scene('game', 
                                                 campaign="default",
                                                 lvl_num=1,
                                                 screen_width=self.screen_w,
                                                 screen_height=self.screen_h)

        
        
if __name__ == '__main__':
    app = App()  