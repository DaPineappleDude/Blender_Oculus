import bpy
import csv
import bmesh
import mathutils
from numpy import pi



#Delete Earlier Cameras
for ob in bpy.context.scene.objects:
    ob.select = ob.type == 'CAMERA' and ob.name.startswith("Camera")
bpy.ops.object.delete()

#Render Settings
bpy.data.scenes["Scene"].render.resolution_x = 4000
bpy.data.scenes["Scene"].render.resolution_y = 3096
bpy.data.scenes["Scene"].render.pixel_aspect_x = 1
bpy.data.scenes["Scene"].render.pixel_aspect_y = 1


#Extracting Data from Test Params

#Camera Location
csv_path = ('/Users/ssambuddha/Documents/MATLAB/camera_location.csv')
with open(csv_path) as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    x = []
    y = []
    z = []
    
    for row in readCSV:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

#Camera Rotation
csv_path = ('/Users/ssambuddha/Documents/MATLAB/camera_rotation.csv')
with open(csv_path) as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    T = {}
    idx  = 0
    
    for row in readCSV:
        
        T_x = []
        T_y = []
        T_z = []
    
        
        T_x = mathutils.Vector([float(row[0]), float(row[1]), float(row[2])])
        T_y = mathutils.Vector([float(row[3]), float(row[4]), float(row[5])])
        T_z = mathutils.Vector([float(row[6]), float(row[7]), float(row[8])])
        

        T[idx] = mathutils.Matrix([T_x, T_y, T_z])
        idx +=1



for cam in range(0, len(x)):
    
    #Setting up cameras in the scene

    if cam > 99:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.active_object
        cam_obj.name = 'Camera.' + str(cam)

    elif cam > 9:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.active_object
        cam_obj.name = 'Camera.0' + str(cam)
        
    elif cam <= 9:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.active_object
        cam_obj.name = 'Camera.00' + str(cam)

    cam_obj.scale = [.06, .06, .06]

    cam_dat = bpy.data.cameras[cam] 
    cam_dat.name = cam_obj.name
    #Focusing the camera
    cam_dat.dof_object = bpy.data.objects['Icosphere']
    cam_dat.type = 'PERSP'
    
    #CAMERA INTRINSICS
    cam_dat.lens = 32 #in mm
    #cam_dat.sensor_width = 
    #cam_dat.sensor_height = 


    #CAMERA EXTRINSICS
    #Positioning the Camera
    cam_obj.location = x[cam], y[cam], z[cam]

    #Rotating the Camera
    T_cam = T[cam]
    T_cam[2] = -T_cam[2]
    T_tmp = T_cam.copy()
    T_cam = T_cam.to_euler()
    cam_obj.rotation_euler = T_cam
    T_tmp.transpose()
    bpy.ops.transform.rotate(value=pi, axis=(T_tmp[2][0], T_tmp[2][1], T_tmp[2][2]), constraint_axis=(False, False, True), constraint_orientation = 'NORMAL')
    #Correction for Cece's axes

