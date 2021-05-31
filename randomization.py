# -*- coding:utf-8 -*-
import bpy, sys, os, math, random

RAND = 10 # number of different combinations to try out

imageFolder = "/images"
lighting = bpy.data.lights["Point"]

for collection in bpy.data.collections:
   print(collection.name)
   for obj in collection.all_objects:
      print("obj: ", obj.name)

if not os.path.exists(imageFolder):
    os.mkdir(imageFolder)

if os.path.exists(imageFolder):
    imageBaseName = bpy.path.basename(imageFolder)
    
    for i in range(RAND):
        bpy.context.scene.render.filepath = os.path.join(imageFolder, str(i) + '-' + imageBaseName)
        # randomize light settings:
        # randomize colors of light: [0, inf], default = (1.0, 1.0, 1.0)
        colors = (255*random.random(), 255*random.random(), 255*random.random())
        lighting.color = colors
        
        # randomize intensity of light: [0, inf], default = 10
        energy = 50 * random.random()
        lighting.energy = energy
        
        # randomize falloff distance of light: [0, inf], default = 25
        lighting.distance = 100 * random.random()
        
        # randomize specular reflection multiplier: [0, 9999], default = 1.0
        # lighting.specular_factor = 9999 * random.random()
        
        print("Rendering and saving animation to " + imageBaseName + "... (this could take a while)")
        colorStr = ""
        for color in colors:
            colorStr += str(color)
        print("lighting colors: " + colorStr)
        print("lighting energy: " + str(energy))
        bpy.ops.render.render(animation = True)
        print("Finished saving!")
else:
    print("Folder does not exist")
    
    
