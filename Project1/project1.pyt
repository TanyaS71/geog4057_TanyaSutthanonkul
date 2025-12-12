import arcpy
from class_activity2 import json2shape     # Import the function you defined

class Toolbox(object):
    def __init__(self):
        """Convert JSON data to a shapefile using ArcPy"""
        self.label = "Convert JSON to Shapefile Toolbox"
        self.alias = "ConvertJSONToShapefile"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "JSON to Shapefile Converter"
        self.description = "Converts a JSON file with WKT geometry into a polygon shapefile."

    def getParameterInfo(self):
        """Define the tool parameters."""

        # Parameter 1: Input JSON file
        param0 = arcpy.Parameter(
            displayName="Input JSON File",
            name="input_json",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")

        # Parameter 2: Output workspace (folder)
        param1 = arcpy.Parameter(
            displayName="Output Workspace",
            name="workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        # Parameter 3: Output Shapefile Name
        param2 = arcpy.Parameter(
            displayName="Output Shapefile Name",
            name="fcname",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # Optional: Spatial reference (default 4236)
        param3 = arcpy.Parameter(
            displayName="Spatial Reference (WKID)",
            name="wkid",
            datatype="GPLong",
            parameterType="Optional",
            direction="Input")
        param3.value = 4236   # Default value

        return [param0, param1, param2, param3]


    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True


    def updateParameters(self, parameters):
        """Modify parameter values before validation."""
        return


    def updateMessages(self, parameters):
        """Modify messages created during validation."""
        return


    def execute(self, parameters, messages):
        """Execution: run the JSON-to-shapefile function."""

        input_json = parameters[0].valueAsText
        workspace = parameters[1].valueAsText
        fcname = parameters[2].valueAsText
        wkid = int(parameters[3].valueAsText) if parameters[3].value else 4236

        # Call your function from class_activity2.py
        json2shape(input_json, workspace, fcname, wkid)

        messages.addMessage("Conversion completed successfully.")
        return


    def postExecute(self, parameters):
        """Actions after tool execution."""
        return
