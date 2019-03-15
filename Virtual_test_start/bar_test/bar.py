# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.3.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/u1449908/Salome_files/Virtual_test_start/bar_test')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(0.000000, 0.000000)
sk.addSegmentAbsolute(0.000000, 10.000000)
sk.addSegmentAbsolute(10.000000, 10.000000)
sk.addSegmentAbsolute(10.000000, 0.000000)
sk.close()
Sketch_1 = sk.wire(geomObj_1)
Face_1 = geompy.MakeFaceWires([Sketch_1], 1)
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Face_1, geompy.ShapeType["FACE"])
Extrusion_1 = geompy.MakePrismVecH2Ways(Face_1, OZ, 50)
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Extrusion_1, geompy.ShapeType["EDGE"])
border = geompy.CreateGroup(Face_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(border, [3, 6, 8, 10])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(border, geompy.ShapeType["EDGE"])
Partition_1 = geompy.MakePartition([Extrusion_1], [Face_1], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["VERTEX"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["FACE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(Partition_1, geompy.ShapeType["EDGE"])
load = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(load, [50])
fix = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(fix, [14])
cen_face = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(cen_face, [11, 30, 25, 28])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sketch_1, 'Sketch_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudyInFather( Face_1, border, 'border' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, load, 'load' )
geompy.addToStudyInFather( Partition_1, fix, 'fix' )
geompy.addToStudyInFather( Partition_1, cen_face, 'cen_face' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Partition_1)
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 2 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetMinSize( 0.5 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
load_1 = Mesh_1.GroupOnGeom(load,'load',SMESH.FACE)
fix_1 = Mesh_1.GroupOnGeom(fix,'fix',SMESH.FACE)
load_2 = Mesh_1.GroupOnGeom(load,'load',SMESH.NODE)
fix_2 = Mesh_1.GroupOnGeom(fix,'fix',SMESH.NODE)
cen_face_1 = Mesh_1.GroupOnGeom(cen_face,'cen_face',SMESH.NODE)
[ load_1, fix_1, load_2, fix_2, cen_face_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ load_2, fix_2, cen_face_1, load_1, fix_1 ] = Mesh_1.GetGroups()
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'/home/u1449908/Salome_files/Virtual_test_start/bar_test/bar_test_Files/RunCase_1/Result-displacement/_ExportedFromSalomeObject_0_1_2_4.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'/home/u1449908/Salome_files/Virtual_test_start/bar_test/bar_test_Files/RunCase_1/Result-displacement/_ExportedFromSalomeObject_0_1_2_4.med', 0, SMESH.MED_V2_2, 1, None ,1)
  pass
except:
  print 'ExportToMEDX() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(load_2, 'load')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(cen_face_1, 'cen_face')
smesh.SetName(fix_2, 'fix')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(fix_1, 'fix')
smesh.SetName(load_1, 'load')

###
### ASTERSTUDY component
###

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
bar_disprmed = MEDReader(FileName='/home/u1449908/Salome_files/Virtual_test_start/bar_test/bar_disp.rmed')

# set active source
SetActiveSource(bar_disprmed)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [933, 668]

# show data in view
bar_disprmedDisplay = Show(bar_disprmed, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# change representation type
bar_disprmedDisplay.SetRepresentationType('Surface LIC')

# change representation type
bar_disprmedDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(bar_disprmedDisplay, ('POINTS', 'reslin__DEPL'))

# rescale color and/or opacity maps used to include current data range
bar_disprmedDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
bar_disprmedDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__DEPL'
reslin__DEPLLUT = GetColorTransferFunction('reslin__DEPL')

# get opacity transfer function/opacity map for 'reslin__DEPL'
reslin__DEPLPWF = GetOpacityTransferFunction('reslin__DEPL')

# set scalar coloring
ColorBy(bar_disprmedDisplay, ('POINTS', 'reslin__DEPL', '2'))

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-190.10745305395832, 5.000000000000002, 0.0]
renderView1.CameraFocalPoint = [5.0, 5.000000000000002, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 2.220446049250313e-16]
renderView1.CameraParallelScale = 50.49752469181039


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
