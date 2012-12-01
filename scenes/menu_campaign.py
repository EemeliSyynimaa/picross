# -*- coding: utf-8 -*-

from engine import scene

class MenuCampaign(scene.Scene):
    """ The menu scene where you choose the campaign. """

    def __init__(self, *args, **kwargs):
        super(MenuCampaign, self).__init__(*args, **kwargs)
        