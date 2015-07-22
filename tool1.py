#copy and paste any of this code into your IDLE window and run as a script to test it
#if you create any new pieces of this in IDLE or ArcGIS, just copy and paste the new code
#after making a change, you can select "Create a new branch..." below, by the green button to make an alternate copy
#after making a change you can also select "Commit directly..." to overwrite the original file

#I like using the comma method for importing multiple modules, as below -Chris
import arcpy, os, env



#below we will wrap the tool in a try-except function so we can generate error messages. I think this is all we need. -Chris
try:
  #not sure if using current workspace is correct, thoughts? -Chris
  env.workspace = "CURRENT"
  
 #In here we will have our actual tool -Chris
 
except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "There has been a nontool error."
