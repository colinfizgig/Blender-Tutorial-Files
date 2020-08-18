# This is a script for placing and constraining bones
# to selected objects.  It is useful for baking physics
# simulations to armatures for export to game engines
# If you use it for something useful please give credit to
# (c) 2020 Colin Freeman
# This code is licensed under MIT license (see LICENSE.txt for details)

#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import bpy

selObj = []

for j in bpy.context.selected_objects:
    selObj.append(j)
    
for i in selObj:
    vg = i.vertex_groups.new(name=i.name)
    verts = []
    for vert in i.data.vertices:
        verts.append(vert.index)
    vg.add(verts, 1.0, 'ADD')
    
bpy.ops.object.armature_add()
bpy.ops.object.editmode_toggle()
bpy.ops.armature.select_all(action='SELECT')
bpy.ops.armature.delete()
    
for e in selObj:
    bpy.ops.armature.bone_primitive_add(name=e.name)
        
bpy.ops.object.posemode_toggle()
bpy.ops.pose.select_all(action='SELECT')

for bone in bpy.context.selected_pose_bones:
    lc = bone.constraints.new(type='COPY_LOCATION')
    lc.target = bpy.data.objects[bone.name]
    rc = bone.constraints.new(type='COPY_ROTATION')
    rc.target = bpy.data.objects[bone.name]

bpy.ops.pose.select_all(action='SELECT')
     
bpy.ops.pose.armature_apply(selected=False)

    
bpy.ops.object.posemode_toggle()