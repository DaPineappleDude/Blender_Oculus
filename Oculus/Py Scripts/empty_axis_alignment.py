import bpy
import mathutils
import bmesh

#Delete Earlier Empties
for ob in bpy.context.scene.objects:
    ob.select = ob.type == 'EMPTY' and ob.name.startswith("Empty")
bpy.ops.object.delete()


face = 0
for face in range(0,19):
    
    # Vertices Data
    V1 = [11,11,11,11,11,1,0,5,5,5,7,2,3,3,3,10,1,2,9]
    V2 = [8,7,6,10,9,5,5,4,9,0,8,3,8,4,2,6,2,6,4]
    V3 = [7,6,10,9,8,10,1,9,10,4,3,0,4,0,7,1,0,7,8]
    
    # Testing for face 1 => v1, v2, v3 = 11, 8, 7
    v1, v2, v3 = V1[face], V2[face], V3[face]

    # Transform Matrix for Icosphere
    T = bpy.data.objects['Icosphere'].matrix_world

    # Local X vector : v2 - v1
    x_vec = bpy.data.objects['Icosphere'].data.vertices[v2].co -bpy.data.objects['Icosphere'].data.vertices[v1].co
    x_vec = mathutils.Vector(x_vec)
    x_vec= T*x_vec
    	
    # Temporary Y vector: v3 - v2
    y_vec = bpy.data.objects['Icosphere'].data.vertices[v3].co - bpy.data.objects['Icosphere'].data.vertices[v1].co
    y_vec = mathutils.Vector(y_vec)
    y_vec = T*y_vec

    # Local Z  vector: cross product of X & Y
    z_vec = x_vec.cross(y_vec)

    # Normalizing Vectors
    x_vec.normalize()
    z_vec.normalize()

    # Local Y vector
    y_vec = z_vec.cross(x_vec)

    # Normalizing Vectors
    y_vec.normalize()

    
    #Naming
    if face > 9 and face < 19:
        #Create Empty
        bpy.ops.object.empty_add(type='ARROWS')
        myobj = bpy.context.active_object
        myobj.name = 'Empty.0' + str(face)
        
    elif face <= 9:
        #Create Empty
        bpy.ops.object.empty_add(type='ARROWS')
        myobj = bpy.context.active_object
        myobj.name = 'Empty.00' + str(face)
        
    
    #Location
    myobj.location = T*bpy.data.objects['Icosphere'].data.vertices[v1].co
    myobj.empty_draw_size = 2

    # Define 3x3 Rotation Matrix in terms of Normal Vectors
    rot_matrix = [[x_vec.x, x_vec.y, x_vec.z], [y_vec.x, y_vec.y, y_vec.z], [z_vec.x, z_vec.y, z_vec.z]]

    rot_matrix = mathutils.Matrix(rot_matrix)

    rot_matrix.transpose()

    # Transforming the Empty to the plane reference
    myobj.rotation_euler = rot_matrix.to_euler()


##Transformation Matrix (Basis)

##Global to Icosphere --> T_Icos
#T_Icos = bpy.data.objects['Icosphere'].matrix_basis


#T_Face = []
##Global to Face_0XX --> T_Face[idx]
#empty_crrnt = 'Empty.0' + idx
#T_Face[idx] = bpy.data.objects[empty_crrnt].matrix_basis

##Icosphere to Face_0XX --> T_I_F
## T_Face[idx] = T_I_F * T_Icos 
#T_Icos_inv = T_Icos.copy()
#T_Icos_inv.inverse()
#T_I_F = T_Face[idx]*T_Icos_inv

##Generating Names for faces
#for idx in range(0, 19):
#    if idx > 9:
#        empty = 'Empty.0' + str(idx)
#    elif idx <= 9:
#        empty = 'Empty.00' + str(idx)
#    print(empty)
    

        