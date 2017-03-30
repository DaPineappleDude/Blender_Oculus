#Render Settings
bpy.data.scenes["Scene"].render.resolution_x = 4000
bpy.data.scenes["Scene"].render.resolution_y = 3096
bpy.data.scenes["Scene"].render.pixel_aspect_x = 1
bpy.data.scenes["Scene"].render.pixel_aspect_y = 1


#Extracting Data from Test Params
cam_loc = 
cam_rot = 


for cam in range(0, len(cam_loc)):
    
    #Setting up cameras in the scene

    if cam_idx > 99:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.active_object
        cam_obj.name = 'Camera.' + str(cam_idx)

    elif cam_idx > 9:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.active_object
        cam_obj.name = 'Camera.0' + str(cam_idx)
        
    elif cam_idx <= 9:
        bpy.ops.object.camera_add()
        cam_obj = bpy.context.active_object
        cam_obj.name = 'Camera.00' + str(cam_idx)

    cam_obj.scale = [.05, .05, .05]

    cam_dat = bpy.data.cameras[cam] 
    cam_dat.name = cam_obj.name
    #Focusing the camera
    cam_dat.dof_object = bpy.data.objects['Icosphere']
    cam_dat.type = 'PERSP'
    
    #CAMERA INTRINSICS
    cam_dat.lens = 32 #in mm
    cam_dat.sensor_width = 
    cam_dat.sensor_height = 


    #CAMERA EXTRINSICS
    #Positioning the Camera
    cam_obj.location = cam_loc[cam]

    #Rotating the Camera
    T_cam = cam_rot[cam]
    T_cam = T_cam.to_euler()
    T_cam[2] = T_cam[2] + pi
    cam_obj.rotation_euler
