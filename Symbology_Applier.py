# Import modules
import arcpy

#Get the current Map Document
mxd = arcpy.mapping.MapDocument("CURRENT")

# Script arguments
Template_Layer = arcpy.GetParameterAsText(0)
Layer = arcpy.GetParameterAsText(1)

arcpy.ApplySymbologyFromLayer_management(Layer,Template_Layer)

# Refresh the Table of Contents to reflect the change
arcpy.RefreshTOC()

#Delete the MXD from memory
del mxd
