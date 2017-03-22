import bpy
import os

#All coordinates in the world frame
#Camera extrinsics
cam_ex = bpy.data.objects["Camera.000"]

cam_position = cam_ex.location
cam_rotation = cam_ex.roation_quaternion
cam_scale = cam_ex.scale


#Camera intrinsics
cam_in = bpy.data.cameras['Camera.000']

cam_f = cam_in.lens
cam_snsr_x = cam_in.sensor_width
cam_snsr_y = cam_in.sensor_height


#Image Settings
res_x = bpy.data.scenes["Scene"].render.resolution_x
res_y = bpy.data.scenes["Scene"].render.resolution_y

aspect_x = bpy.data.scenes["Scene"].render.pixel_aspect_x
aspect_y = bpy.data.scenes["Scene"].render.pixel_aspect_y


#Mesh Data