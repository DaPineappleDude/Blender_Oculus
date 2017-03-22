import sys
import bpy
import os

#All coordinates in the world frame
#Camera extrinsics
"""
cam_ex = bpy.data.objects["Camera.000"]

cam_position = cam_ex.location
cam_rotation = cam_ex.rotation_quaternion
cam_scale = cam_ex.scale
"""

#Camera intrinsics
"""
cam_in = bpy.data.cameras['Camera.000']

cam_f = cam_in.lens
cam_snsr_x = cam_in.sensor_width
cam_snsr_y = cam_in.sensor_height 
"""


#Image Settings
res_x = bpy.data.scenes["Scene"].render.resolution_x
res_y = bpy.data.scenes["Scene"].render.resolution_y

aspect_x = bpy.data.scenes["Scene"].render.pixel_aspect_x
aspect_y = bpy.data.scenes["Scene"].render.pixel_aspect_y


#Mesh Data
ico_obj = bpy.data.meshes['Icosphere']

#Test
for frame in range(scene_info.frame_start, scene_info.frame_end+1):
    scene_info.frame_set(frame)
    print('\nImage Number %i'%frame)
    
    for idx in range(0, len(ico_obj.polygons)):
        print('Normal of Face %i is: %s' %(idx, ico_obj.polygons[idx].normal))


#Test : Print Format
for cam in bpy.data.cameras:
    print('%s\n focal length = %fmm\n sensor width = %fmm\n sensor height = %fmm\n Resolution (Width x Height) = %fX%f px\n' %(cam.name, cam.lens, cam.sensor_width, cam.sensor_height,bpy.data.scenes["Scene"].render.resolution_x, bpy.data.scenes["Scene"].render.resolution_y))
    

'''for cam in bpy.data.objects:
    print('%s has a location of %s & orientation %s' %(cam.name, cam.location, cam.rotation_quaternion))'''
    
print('\n')

num_camera = len(bpy.data.cameras) 

for idx in range(0, num_camera):
    cam = bpy.data.objects[idx]
    #Location
    print('%s is located at:\nCartesian\n x = %fcm\n y = %fcm\n z = %fcm\n' %(cam.name, cam.location.x, cam.location.y, cam.location.z,))
    #Orientation
    print('Quaternion\n w = %f\n x = %f\n y = %f\n z = %f\n' %(cam.rotation_quaternion.w, cam.rotation_quaternion.x, cam.rotation_quaternion.y, cam.rotation_quaternion.z))








#--------------{EXPORT CAMERA DATA\start}---------------------------------

f = open('G:/Blender/camera_data.txt', 'w', encoding= 'utf-8')

#---------------------------{CAMERA INTRINSICS\start}---------------------------------

f.write('CAMERA INTRINSICS\n')

for cam in bpy.data.cameras:
    f.write('\n%s\n focal length = %fmm\n sensor width = %fmm\n sensor height = %fmm\n Resolution (Width x Height) = %fX%f px\n' %(cam.name, cam.lens, cam.sensor_width, cam.sensor_height,bpy.data.scenes["Scene"].render.resolution_x, bpy.data.scenes["Scene"].render.resolution_y))
    

#---------------------------{CAMERA INTRINSICS\end}---------------------------------


#---------------------------{CAMERA EXTRINSICS\start}---------------------------------
    
f.write('\n\nCAMERA EXTRINSICS\n')

num_camera = len(bpy.data.cameras) 

for idx in range(0, num_camera):
    cam = bpy.data.objects[idx]
    #Location
    f.write('\n%s is located at:\nCartesian\n x = %fcm\n y = %fcm\n z = %fcm\n' %(cam.name, cam.location.x, cam.location.y, cam.location.z,))
    #Orientation
    f.write('Quaternion\n w = %f\n x = %f\n y = %f\n z = %f\n' %(cam.rotation_quaternion.w, cam.rotation_quaternion.x, cam.rotation_quaternion.y, cam.rotation_quaternion.z))

#---------------------------{CAMERA EXTRINSICS\end}---------------------------------


f.close()
#--------------{EXPORT CAMERA DATA\end}---------------------------------


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#--------------{EXPORT MESH DATA\start}---------------------------------


#Scene Information
scene_info = bpy.context.scene

#Mesh 
ico_obj = bpy.data.meshes['Icosphere']

     
        
f = ofor frame in range(scene_info.frame_start, scene_info.frame_end+1):
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
        
        
        
        pen('G:/Blender/target_data.txt', 'w', encoding= 'utf-8')
f.write('MESH DATA OF TARGET PER IMAGE')

for frame in range(scene_info.frame_start, scene_info.frame_end+1):
    scene_info.frame_set(frame)
    f.write('\n\nImage Number %i'%frame)
    #Transform Matrix
    T = bpy.data.objects['Icosphere'].matrix_world   
    for idx in range(0, len(ico_obj.polygons)):
        f.write('\nNormal of Face %i is: %s' %(idx, T*ico_obj.polygons[idx].normal))
        
f.close()

#--------------{EXPORT MESH DATA\end}---------------------------------




