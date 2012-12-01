# -*- coding: utf-8 -*-

from engine import scene

class MenuLevel(scene.Scene):
    """ The menu scene where you choose the level. """

    def __init__(self, *args, **kwargs):
        super(MenuLevel, self).__init__(*args, **kwargs)
        