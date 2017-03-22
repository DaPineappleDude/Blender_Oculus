import sys
import bpy
import os
import numpy as np


#Scene Information
scene_info = bpy.context.scene

#Mesh 
ico_obj = bpy.data.meshes['Icosphere']

#Test
for frame in range(scene_info.frame_start, scene_info.frame_end+1):
    scene_info.frame_set(frame)
    print('\n\nImage Number %i'%frame)
    #Transform Matrix : 'asfortranarray' speeds up matrix operations as it does column-major order (like MATLAB)
    T = np.asfortranarray(bpy.data.objects['Icosphere'].matrix_world)
    for idx in range(0, len(ico_obj.polygons)):
        x = ico_obj.polygons[idx].center.x
        y = ico_obj.polygons[idx].center.y
        z = ico_obj.polygons[idx].center.z
        center_vect = np.asfortranarray([[x, y, z, 1.]])
        center_vect = T*center_vect
        print('\nCenter of Face %i is: %s' %(idx, center_vect))
        
        
f = open('G:/Blender/target_data.txt', 'w', encoding= 'utf-8')

for frame in range(scene_info.frame_start, scene_info.frame_end+1):
    scene_info.frame_set(frame)
    f.write('\n\nImage Number %i'%frame)
    #Transform Matrix : 'asfortranarray' speeds up matrix operations as it does column-major order (like MATLAB)
    T = np.asfortranarray(bpy.data.objects['Icosphere'].matrix_world)
    for idx in range(0, len(ico_obj.polygons)):
        x = ico_obj.polygons[idx].center.x
        y = ico_obj.polygons[idx].center.y
        z = ico_obj.polygons[idx].center.z
        center_vect = np.asfortranarray([[x, y, z, 1.]])
        center_vect = T*center_vect
        f.write('\nCenter of Face %i is: %s' %(idx, center_vect))
        

f.close()
        
    
