import bmesh
import bpy
import mathutils
import os

scene = bpy.context.scene
scene.render.image_settings.file_format = 'PNG' # set output format to .png

for cam in range(0, 5):
    
    
    if cam > 99:
        cam_name = 'Camera.' + str(cam)

    elif cam > 9:
        cam_name = 'Camera.0' + str(cam)
        
    elif cam <= 9:
        cam_name = 'Camera.00' + str(cam)

    #Set Active Camera
    scene.camera = bpy.data.objects[cam_name]
    
    fname = '/Users/ssambuddha/Blender_Oculus/Oculus/Hatem_Test/'
    fname += cam_name + '/'
    scene.render.filepath = fname
    fp = scene.render.filepath

    for frm in range(0,50):

        scene.frame_set(frm)

        # set output path so render won't get overwritten
        scene.render.filepath = fp + str(frm)
        bpy.ops.render.render(write_still=True) # render still
