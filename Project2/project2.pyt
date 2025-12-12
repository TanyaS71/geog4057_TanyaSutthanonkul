# -*- coding: utf-8 -*-

import arcpy
from project2 import project2


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Project 2 Toolbox"
        self.alias = "project2"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        params0 = arcpy.Parameter(
            displayName="CSV File",
            name="csv_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        #params1 is a shapefile name
        param1 = arcpy.Parameter(
            displayName="shapefile",
            name="shapefile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        #params2 is a raster dataset
        param2 = arcpy.Parameter(
            displayName="raster data",
            name="raster_data",
            datatype="DERasterDataset",
            parameterType="Required",
            direction="Input")
        #params3 is a string
        param3 = arcpy.Parameter(
            displayName="project name",
            name="project_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        params = [params0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        csv_file = parameters[0].valueAsText
        shapefile = parameters[1].valueAsText
        raster_file = parameters[2].valueAsText
        project_name = parameters[3].valueAsText
        project2(project_name, csv_file, raster_file, shapefile)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return