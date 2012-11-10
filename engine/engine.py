import pyglet

from scene_manager import SceneManager

class Engine(pyglet.window.Window):
    """ The main engine class. """
    def __init__(self, *args, **kwargs):
        super(Engine, self).__init__(*args, **kwargs)
        
        self.scene_manager = SceneManager(engine=self)
        self.fps = pyglet.clock.ClockDisplay()
        
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        
    def add_resource_path(self, location):
        pyglet.resource.path.append(location)
        pyglet.resource.reindex()
    
    def update(self, dt):
        pass
    
    def run(self):
        pyglet.app.run()
        
    def on_draw(self):
        self.clear()
        self.fps.draw()
        self.scene_manager.on_draw()