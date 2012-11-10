import pyglet

import scene_manager

class Engine(pyglet.window.Window):
    """ The main engine class. """
    def __init__(self, *args, **kwargs):
        super(Engine, self).__init__(*args, **kwargs)
        self.scene_manager = scene_manager.SceneManager()
        self.fps = pyglet.clock.ClockDisplay()
        
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        
        pyglet.app.run()
    
    def update(self, dt):
        pass
    
    def on_draw(self):
        self.clear()
        
        self.scene_manager.on_draw()
        
        self.fps.draw()