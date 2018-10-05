from sys import exit
from random import randint
from textwrap import dedent

class Scene():

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine():
    def __init__(self, scene_man):
        self.scene_map = scene_map

    def paly(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene_man
        current_scene.enter()
        
