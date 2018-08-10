#!/usr/bin/env python
 
import vtk
import os
 
def vtp_to_stl(file_in, file_out):
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(file_in)
    writer = vtk.vtkSTLWriter()
    writer.SetFileName(file_out)
    writer.SetFileTypeToBinary();
    writer.SetInputConnection(reader.GetOutputPort())
    writer.Write()

DIR_IN = "osim-rl/osim/models/Geometry/"
DIR_OUT = "mujoco-rl/models/Geometry/"

for filename in os.listdir(DIR_IN):
    if not filename.endswith(".vtp"):
        continue
    file_in = DIR_IN + filename
    file_out = DIR_OUT + os.path.splitext(filename)[0] + ".stl"
    vtp_to_stl(file_in,file_out)
