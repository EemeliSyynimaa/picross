import pyglet

class Engine:
    """ The main engine class. """
    def __init__(self):
        """ Initializes the engine. """
        
        self.screen = pyglet.window.Window(width=1280, height=720)
        
        pyglet.app.run()
    
    def update(self):
        """ Updates all game actions. """
        pass
    
    def draw(self):
        """ Draws all the stuff. """
        pass