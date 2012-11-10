#!/usr/bin/env python

import engine

class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.engine = engine.Engine(width=1280, height=720)
        
if __name__ == '__main__':
    app = App()  