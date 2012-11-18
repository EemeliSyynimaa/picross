# -*- coding: utf-8 -*-

import level

from engine import scene

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
   
    def on_draw(self):
        self.batch.draw()
        self.level.draw()