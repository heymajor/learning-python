# Alien
# Player
# Ship
# Maze
# Scene
# Gothon
# Escape Pod
# Planet
# Engine
# Death
# Central Corridor
# Laser Weapon Armory
# The Bridge


# Map
#     - next_scene
#     - opening_scene
# Engine
#     - play
# Scene
#     - enter
#     Death
#     Central Corridor
#     Laser Weapon Armory
#     The Bridge
#     Escape Pod


class Scene(object):
	def enter(self):
		pass

class Engine(object):
	def play(self, scene_map):
		pass

class Death(Scene):
	def enter(self):
		pass

class CentralCorridor(Scene):
	def enter(self):
		pass

class LaserWeaponArmory(Scene):
	def enter(self):
		pass

class TheBridge(Scene):
	def enter(self):
		pass

class EscapePod(Scene):
	def enter(self):
		pass

class Map(object):
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass