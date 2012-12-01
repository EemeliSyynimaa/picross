#!/usr/bin/env python
# -*- coding: utf-8 -*-

from engine import engine
from scenes import game
from scenes import game_won
from scenes import game_lost

class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.engine = engine.Engine(width=1280, height=720,
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
        self.engine.scene_manager.activate_scene('game', 
                                                 campaign="default",
                                                 lvl_num=1,
                                                 screen_width=1280,
                                                 screen_height=720)

        
        
if __name__ == '__main__':
    app = App()  