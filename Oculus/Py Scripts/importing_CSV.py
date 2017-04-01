import csv
import bpy
 
##Camera Location

#csv_path = ('/Users/ssambuddha/Documents/MATLAB/camera_location.csv')
#with open(csv_path) as csvfile:
#    readCSV = csv.reader(csvfile, delimiter = ',')
#    
#    x = []
#    y = []
#    z = []
#    
#    for row in readCSV:
#        x.append(float(row[0]))
#        y.append(float(row[1]))
#        z.append(float(row[2]))
#        
##Camera Rotation

#csv_path = ('/Users/ssambuddha/Documents/MATLAB/camera_rotation.csv')
#with open(csv_path) as csvfile:
#    readCSV = csv.reader(csvfile, delimiter = ',')
#    
#    T = {}
#    idx  = 0
#    
#    for row in readCSV:
#        
#        T_x = []
#        T_y = []
#        T_z = []
#        
#        T_x = mathutils.Vector([float(row[0]), float(row[1]), float(row[2])])
#        T_y = mathutils.Vector([float(row[3]), float(row[4]), float(row[5])])
#        T_z = mathutils.Vector([float(row[6]), float(row[7]), float(row[8])])
#        

#        T[idx] = mathutils.Matrix([T_x, T_y, T_z])
#        idx +=1


#Icosphere Location

csv_path = ('/Users/ssambuddha/Documents/MATLAB/icosphere_location_695.csv')
with open(csv_path) as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    I_x = []
    I_y = []
    I_z = []
    
    for row in readCSV:
        I_x.append(float(row[0]))
        I_y.append(float(row[1]))
        I_z.append(float(row[2]))
        
for pos in range(0, len(I_x)):
    bpy.context.scene.frame_set(pos)
    ico = bpy.data.objects['Icosphere']
    ico.location = I_x[pos],I_y[pos],I_z[pos]
    ico.keyframe_insert(data_path="location", index=-1)
    empty = bpy.data.objects['Empty.Icosphere']
    empty.location = I_x[pos],I_y[pos],I_z[pos]
    empty.keyframe_insert(data_path="location", index=-1)