#Moving vertices in global coordinates

import bpy


obj  = bpy.data.objects['Cube']
mesh = obj.data
vert = mesh.vertices[0]
mat_world = obj.matrix_world

pos_world = mat_world * vert.co
pos_world.z += 0.1
vert.co = mat_world.inverted() * pos_world

#If you're editing a lot of vertices then you might want to compose the matrix:

from mathutils import Vector, Matrix

vec = Vector((0.0, 0.0, 0.1))  
mat_edit = mat_world.inverted() * Matrix.Translate(vec) * mat_world

vert.co = mat_edit * vert.co


#Current Vertice Display
import bmesh
def print_vert_details(selected_verts):
	num_verts = len(selected_verts)
	print("number of verts: {}".format(num_verts))
	print("vert indices: {}".format([id.index for id in selected_verts]))
def get_vertex_data(object_reference):
	bm = bmesh.from_edit_mesh(object_reference.data)
	selected_verts = [vert for vert in bm.verts if vert.select]
	print_vert_details(selected_verts)

#Function Call
#object_reference = bpy.context.active_object
#get_vertex_data(object_reference)


#Aligning an empty along a vector
Vector = bpy.data.objects['Icosphere.002'].data.vertices[10].co - bpy.data.objects['Icosphere.002'].data.vertices[11].co
DirectionVector = mathutils.Vector(Vector) 
bpy.context.object.rotation_mode = 'QUATERNION'
bpy.context.object.rotation_quaternion = DirectionVector.to_track_quat('X','Z')

bpy.data.objects[ok].rotation_mode



def frame_rot(empty, v1, v2, axis1, axis2):
	
	Vec = bpy.data.objects['Icosphere.002'].data.vertices[v1].co - bpy.data.objects['Icosphere.002'].data.vertices[v2].co
	DirectionVector = mathutils.Vector(Vec)
	bpy.data.objects[empty].rotation_mode = 'QUATERNION'
	bpy.data.objects[empty].rotation_quaternion = DirectionVector.to_track_quat(axis1, axis2)
	bpy.data.objects[empty].location = bpy.data.objects['Icosphere.002'].data.vertices[v2].co
	bpy.data.objects[empty].location = bpy.data.objects['Icosphere.002'].matrix_world*bpy.data.objects['Icosphere.002'].data.vertices[v2].co 






#Mesh 
ico_obj = bpy.data.meshes['Icosphere']

		
		
f = open('G:/Blender/target_data.txt', 'w', encoding= 'utf-8')
f.write('MESH DATA OF TARGET PER IMAGE')

for frame in range(scene_info.frame_start, scene_info.frame_end+1):
	scene_info.frame_set(frame)
	f.write('\n\nImage Number %i'%frame)
	
	for idx in range(0, len(ico_obj.polygons)):
		f.write('\nNormal of Face %i is: %s' %(idx, ico_obj.polygons[idx].normal))


empty = 'Empty'
DirectionVector = mathutils.Vector(bpy.data.meshes['Icosphere.002'].polygons[5].normal)
bpy.data.objects[empty].rotation_mode = 'QUATERNION'
bpy.data.objects[empty].rotation_quaternion = DirectionVector.to_track_quat('X', 'Z')


#Get current face & vertices index
def vertices():
	bm = bmesh.from_edit_mesh(bpy.context.active_object.data)
	selected_face = bm.faces
	selected_verts = [poly for poly in bm.verts if poly.select]
	num_verts = len(selected_verts)
	print("vert indices: {}".format([id.index for id in selected_verts]))

def face_idx():
	obj = bpy.context.edit_object
	me = obj.data
	bm = bmesh.from_edit_mesh(me)

	for f in bm.faces:
		if f.select:
			print(f.index)






# Rotating empty
def frame_rot(empty, v1, v2, v3):

	#Relocating Empty to Vertice
	bpy.data.objects[empty].location = bpy.data.objects['Icosphere'].matrix_world*bpy.data.objects['Icosphere'].data.vertices[v2].co
	x_vec = bpy.data.objects['Icosphere'].data.vertices[v2].co - bpy.data.objects['Icosphere'].data.vertices[v1].co
	DirectionVector_x = mathutils.Vector(x_vec)
	

	y_vec_intrim = bpy.data.objects['Icosphere'].data.vertices[v3].co - bpy.data.objects['Icosphere'].data.vertices[v1].co
	DirectionVector_y_intrim = mathutils.Vector(y_vec_intrim)


	z_vec = mathutils.CrossVecs(x_vec, y_vec_intrim)

	x_vec.normalize()
	z_vec.normalize()
	y_vec = mathutils.CrossVecs(z_vec, x_vec)


	



