#!/usr/bin/env python
# -*- coding: utf-8 -*-

from engine import engine
from scenes import game

class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.engine = engine.Engine(width=1280, height=720)
        self.engine.scene_manager.add_scene("game", game.Game)
        
        self.engine.run()
        
if __name__ == '__main__':
    app = App()  