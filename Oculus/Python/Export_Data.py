import sys
import bpy
import os


#Scene Information
scene_info = bpy.context.scene

#Mesh Data
ico_obj = bpy.data.objects['Icosphere']


ico_obj.data.polygons[1]

#Test
for cam in bpy.data.cameras:
    print('%s\n focal length = %fmm\n sensor width = %fmm\n sensor height = %fmm\n Resolution (Width x Height) = %fX%f px\n' %(cam.name, cam.lens, cam.sensor_width, cam.sensor_height,bpy.data.scenes["Scene"].render.resolution_x, bpy.data.scenes["Scene"].render.resolution_y))
    



