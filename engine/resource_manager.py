import yaml
import pyglet

class ResourceManager(object):
    """ This class holds recources the game uses. """

    def __init__(self):
        pass

    def load_yaml(self, location):
        temp = yaml.load(location)
        
        var = {}   
        var[file.split('.')[0]] = {}
                
        for key in temp.keys():
            var[file.split('.')[0][key]] = temp[key]
            
        return var

    def load_image(self, image, location=None):
        if location:
            temp_loader = pyglet.resource.Loader(location)
            temp = temp_loader.image(image)
        else:
            temp = pyglet.resource.image(image)
        
        name = image.split('.')[0]
        return temp
        
    def load_media(self, sound, location=None):
        if location:
            temp_loader = pyglet.resource.Loader(location)
            temp = temp_loader.media(sound)
        else:
            temp = pyglet.resource.media(sound)
        
        name = sound.split('.')[0]
        return temp
        