# -*- coding: utf-8 -*-

from engine import scene

class GameWon(scene.Scene):
    """ The scene which comes after the great success in Game scene. """

    def __init__(self, manager, campaign, lvl_num,
                 screen_width, screen_height, *args, **kwargs):
        super(GameWon, self).__init__(manager, *args, **kwargs)
        
        self.campaign = campaign
        self.lvl_num = lvl_num
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.init_resources()
        
    def init_resources(self):
        self.resource_manager.load_image(str(self.lvl_num) + ".png", 
                                         "levels\\" + self.campaign)
        
    def on_draw(self):
        x = self.screen_width/2 - \
            self.resource_manager.gfx[str(self.lvl_num)].width/2
        y = self.screen_height/2 - \
            self.resource_manager.gfx[str(self.lvl_num)].height/2
        self.resource_manager.gfx[str(self.lvl_num)].blit(x, y)