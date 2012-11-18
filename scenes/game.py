# -*- coding: utf-8 -*-

import level

from engine import scene
from pyglet.window import mouse

class Game(scene.Scene):
    """ The class that makes the game go on. """

    def __init__(self, manager, path):
        super(Game, self).__init__(manager)
        
        self.level = level.Level(path, self.resource_manager, 1280/2, 720/2)
        self.init_resources()
        
        #
        #
        #
        #
        # TODO
        #
        #
        # Eriytä PLAYGRID ja ORIGINALGRID omiin luokkiinsa!!
        #
        # WILL DO!
        
    def init_resources(self):
        pass
    
    def update(self, dt):
        if self.level.check_victory_conditions():
            print("GAME WON!")
    
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