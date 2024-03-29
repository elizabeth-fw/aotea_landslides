import os
import sys

sys.path.append("C:/Users/tdow214/OneDrive - The University of Auckland/Documents/GitHub/aotea_landslides")
from Landsat import read_shapefile, clip_tar_raster

# Directories
img_base_dir = "Z:/Raw_data/Aotea/"
vector_base_dir = "C:/Users/tdow214/OneDrive - The University of Auckland/Documents/Projects/Landslides/"
img_drv_dir = "Z:/Derived_data/Aotea_landslides/"
tmp_dir = os.path.join(img_base_dir, "tmp_dir")
if not os.path.exists(tmp_dir):
    os.mkdir(tmp_dir)


# Import AOI
aoi_path = os.path.join(vector_base_dir,
                        "Aotea_AOI.shp")
aotea_aoi = read_shapefile(aoi_path)


# Import Landsat Data
landsat_ard_dir = os.path.join(img_drv_dir, "landsat_ard")
if not os.path.exists(landsat_ard_dir):
    os.mkdir(landsat_ard_dir)

tar_file = os.path.join(img_base_dir,
                        "Landsat/2023/LC08_L1TP_073085_20231101_20231109_02_T1.tar")

clip_tar_raster(tar_file, tmp_dir, aotea_aoi)


# Functions - Apply Scaling Factors


# Functions - Cloud Masking


# Functions - Visualizations


# Data Processing and Composite Creation
