import os
import sys

sys.path.append("C:/Users/ewil195/PycharmProjects/aotea_landslides")
from Landsat import read_shapefile, clip_tar_raster, process_all_tar_files

# Directories
img_base_dir = "Z:/Raw_data/Aotea/"
vector_base_dir = "C:/Users/ewil195/PycharmProjects/aotea_landslides/"
img_drv_dir = "Z:/Derived_data/Aotea_landslides/"
tmp_dir = os.path.join(img_base_dir, "tmp_dir")
if not os.path.exists(tmp_dir):
    os.mkdir(tmp_dir)


# Import AOI
aoi_path = os.path.join(vector_base_dir,
                        "aotea_shp/aotea.shp")
aotea_aoi = read_shapefile(aoi_path)

"""
# Import and Clip Landsat Data
landsat_ard_dir = os.path.join(img_drv_dir, "landsat_ard")
if not os.path.exists(landsat_ard_dir):
    os.mkdir(landsat_ard_dir)

tar_file = os.path.join(img_base_dir,
                        "Landsat/2023/LC08_L1TP_073085_20231101_20231109_02_T1.tar")

clip_tar_raster(tar_file, tmp_dir, aotea_aoi)
"""

# Process all TAR files
#landsat_dir = os.path.join(img_drv_dir, "Landsat")

process_all_tar_files(img_base_dir, img_drv_dir, aotea_aoi)


# Functions - Apply Scaling Factors

## could clip & scale in one function
## add another subfolder of each image within year

# Functions - Cloud Masking


# Export TIF with scaling & cloudmasking in one


# Functions - Visualizations

## optimize for me seeing landslides
## only have three channels - how to work with bands in those
## read on what is the best combination for viewing landslides - landslide optimized false color image

# Data Processing and Composite Creation
