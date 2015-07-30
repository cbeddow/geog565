#copy and paste any of this code into your IDLE window and run as a script to test it
#if you create any new pieces of this in IDLE or ArcGIS, just copy and paste the new code
#after making a change, you can select "Create a new branch..." below, by the green button to make an alternate copy
#after making a change you can also select "Commit directly..." to overwrite the original file

#I like using the comma method for importing multiple modules, as below -Chris
#Thats a good one.  Seems more efficient -Sara
import arcpy, os, env



#below we will wrap the tool in a try-except function so we can generate error messages. I think this is all we need. -Chris
try:
  #not sure if using current workspace is correct, thoughts? -Chris
  #I have been thinking that "CURRENT" was only to be used in the Python window of ArcMap??? -Sara
  #I think that's right, so going to code it out -Chris
  ##env.workspace = "CURRENT"
  
 #In here we will have our actual tool -Chris
 
 #added function below that is a start on calculating FAA regions using the state
 # called Flight Standards District Office (FSDO) regions
 # sources: https://www.faa.gov/mobile/index.cfm?event=office.regions
 # what is a pain is that some counties in Kentucky and Illinois are part of a different region than the rest of the state
 # we can fix this by finding the zip codes for those counties and adding it to the region
 # alternate idea is we can get an FSDO shapefile made first, and after geocoding we can use "clip" based on geometry instead of the below example
def FSDOfinder(state):
northwest = [CO, ID, MT, OR, UT, WA, WY]
for state in states:
  if state in northwest:
    FAAregion = "NW":
#incomplete code above, would need a cursor funciton to update rows in a blank "FSDO" field
#I think making an FSDO (or finding one) shapefile and clipping will be more efficient after geocoding into XY point data
 
except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "There has been a nontool error."
