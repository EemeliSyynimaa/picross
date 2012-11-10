import yaml
import pyglet

class ResourceManager(object):
    """ This class holds recources the game uses. """

    def __init__(self):
        self.var = {}
        self.gfx = {}
        self.sfx = {}

    def load_yaml(self, location):
        temp = yaml.load(location)
                
        self.var[file.split(".")[0]] = {}
                
        for key in temp.keys():
            self.var[file.split(".")[0][key]] = temp[key]

    def load_image(self, image):
        temp = pyglet.resource.image(image)
        
        name = image.split('.')[0]
        self.gfx[name] = temp
        
    def load_media(self, sound):
        temp = pyglet.resource.media(sound)
        
        name = sound.split('.')[0]
        self.sfx[name] = temp
        