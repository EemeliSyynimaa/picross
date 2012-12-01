# -*- coding: utf-8 -*-

from engine import scene

class GameLost(scene.Scene):
    """ A scene which appears after a lost game. """

    def __init__(self, *args, **kwargs):
        super(GameLost, self).__init__(*args, **kwargs)
        