import yaml
import pyglet
    
class SfxManager(dict):
    """ This class stores media content. """
    def __init__(self, *args, **kwargs):
        super(SfxManager, self).__init__(*args, **kwargs)
        
    def load_media(self, sound, location=None):
        temp = None
        
        if location:
            temp_loader = pyglet.resource.Loader(location)
            temp = temp_loader.media(sound)
        else:
            temp = pyglet.resource.media(sound)
        
        name = sound.split('.')[0]
        self[name] = temp
        
class VarManager(dict):
    """ This class stores text content. """
    def __init__(self, *args, **kwargs):
        super(VarManager, self).__init__(*args, **kwargs)
        
    def load_yaml(self, location):
        temp = yaml.load(location)
         
        self[file.split('.')[0]] = {}
                
        for key in temp.keys():
            self[file.split('.')[0][key]] = temp[key]
            
            
class GfxManager(dict):
    """ This class stores graphic content. """
    
    def __init__(self, *args, **kwargs):
        super(GfxManager, self).__init__(*args, **kwargs)
        
    def load_image(self, image, location=None):
        temp = None
        
        if location:
            temp_loader = pyglet.resource.Loader(location)
            temp = temp_loader.image(image)
        else:
            temp = pyglet.resource.image(image)
        
        name = image.split('.')[0]
        self[name] = temp
        