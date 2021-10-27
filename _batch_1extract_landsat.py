# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# _batch_1extract_landsat.py
# Created on: 2020-03-28 12:30:24.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: _batch_1extract_landsat 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy import env
import os, glob, sys

## setting this before run  ##
#indirTile = r"G:\product\GFC2017\02a_1deg"
indirTile = r"E:\GLAD\wuhan_metricsA"
outdirTab = r"E:\project\wuhan\sample_data\metricsA"
indirShp = r"E:\project\wuhan\sample_data\shp"
strSearch = '*.tif'
#strSearch = '*red_min_RN.tif'
#strSearch = '*red_av75smax.tif'
#strSearch = '*nir_avsmin25.tif'
extMethod = "INTERPOLATE"

tileList = ['112E_30N', '115E_30N',
            '113E_29N', '113E_30N', '113E_31N', '114E_29N', '114E_30N', '114E_31N',
            '115E_29N', '115E_31N', '116E_29N', '116E_30N', '116E_31N']
#tileList = ['115E_30N']
#tileList = ['113E_27N']
field = "FIDs" # value should be 1

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

if not os.path.exists(outdirTab):
        os.makedirs(outdirTab)
env.workspace = outdirTab

for inTile in tileList:
        print(" tile: {0}".format(inTile))
        
        print('  method: {0}'.format(extMethod))
        indirRst = os.path.join(indirTile, inTile)
        os.chdir(indirRst)
        rstList = glob.glob(strSearch)
        #print (rstList)
        
        outdir = os.path.join(outdirTab, inTile)
        if not os.path.exists(outdir):
                os.makedirs(outdir)
        i = 0
        for inRst in rstList:
                i = i+1
                print(" band: {0}".format(inRst))
                inShp = os.path.join(indirShp, inTile+'.shp')
                saRst = os.path.join(indirRst, inRst)                
                fileName = inRst.replace('.tif', '')
                fileName = fileName.replace('2019_', '')
                ouShp = os.path.join(outdir, fileName + '.shp')
                
                print('Input shape: {0}'.format(inShp))
                print('Input raster: {0}'.format(saRst))
                print('Output shape: {0}'.format(ouShp))
                print(i)
                arcpy.gp.ExtractValuesToPoints_sa(inShp, saRst, ouShp, extMethod, "VALUE_ONLY")
	

#arcpy.gp.ExtractValuesToPoints_sa("G:/project/hunan1718/data/field/plot_pt/deg/113E_28N.shp",
#                                  "G:/product/ARD/Metrics/113E_28N/2017_blue_av2575.tif",
#                                  "G:/project/hunan1718/data/field/extvalue/test/l8blue_bi.shp",
#                                  "INTERPOLATE", "VALUE_ONLY")