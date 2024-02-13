import fiona
import os
from shapely.geometry import shape
import tarfile
import rasterio
from rasterio.mask import mask
from rasterio.plot import show
from rasterio.windows import Window
import glob
import sys

sys.path.append("C:/Users/ewil195/PycharmProjects/aotea_landslides")
from data_handling import reproject_raster


# Functions
def read_shapefile(fpath):
    """
    Read a shapefile
    :param fpath:
    :return:
    """
    with fiona.open(fpath, "r") as src:
        feature = next(iter(src))
        aoi = shape(feature["geometry"])
        return aoi


def extract_tar(tar_file, extract_folder):
    # Get a list of file names in the tar archive
    with tarfile.open(tar_file, "r") as tar:
        file_names_in_tar = tar.getnames()

    # Check if each file already exists in teh destination folder
    files_to_extract = []
    for i in file_names_in_tar:
        dest_path = os.path.join(extract_folder, i)
        if not os.path.exists(dest_path):
            files_to_extract.append(i)

    # Extract the files that do not alreayd exist in the destination folder
    if files_to_extract:
        with tarfile.open(tar_file, "r") as tar:
            tar.extractall(path=extract_folder,
                           members=[member for member in tar.getmembers() if member.name in files_to_extract])
        print ("Contents of", tar_file, "extracted to", extract_folder)
    else:
        print("All files from", tar_file, "already exist in", extract_folder)


def clip_raster_aoi(raster_file, aoi_geom, output_file):
    with rasterio.open(raster_file) as src:
        clipped_img, clipped_transform = mask(src, [aoi_geom], crop=True)
        clipped_meta = src.meta.copy()
        clipped_meta.update({
            "driver": "GTiff",
            "height": clipped_img.shape[1],
            "width": clipped_img.shape[2],
            "transform": clipped_transform})
    with rasterio.open(output_file, "w", **clipped_meta) as dst:
        dst.write(clipped_img)
    print("Clipped raster saved to:", output_file)


def clip_tar_raster(tar_file, extract_folder, aoi_geom, output_folder):
    extract_tar(tar_file, extract_folder)
    band_paths = glob.glob(os.path.join(extract_folder, "*.tif"))
    print(band_paths)
    for j in band_paths:
        new_fpath = j.split(".")[0]+"_r.tif"
        with rasterio.open(j) as src:
            reproject_raster(src, new_fpath, 2193)
        os.remove(j)
    band_paths = glob.glob(os.path.join(extract_folder, "*.tif"))
    print(band_paths)
    for i in band_paths:
        band_name = os.path.basename(i)
        output_file = os.path.join(output_folder, band_name)
        clip_raster_aoi(i, aoi_geom, output_file)



