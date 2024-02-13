import rasterio
from rasterio.warp import calculate_default_transform, reproject


def reproject_raster(src_file, output_file, aoi_crs=2193):
    """
    Reprojects a raster to match the CRS of the AOI.

    :param src_file: Path to the source raster file.
    :param output_file: Path to save the reprojected raster.
    :param aoi_crs: CRS of the AOI (default: EPSG 2193).
    """
    # Open the source raster
    with rasterio.open(src_file) as src:
        # Get the CRS of the source raster
        src_crs = src.crs

        # Calculate the transform and dimensions for reprojection
        transform, width, height = calculate_default_transform(src_crs, aoi_crs, src.width, src.height, *src.bounds)

        # Update metadata for the reprojected raster
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': aoi_crs,
            'transform': transform,
            'width': width,
            'height': height})

        # Reproject the raster
        with rasterio.open(output_file, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=aoi_crs,
                    resampling=rasterio.enums.Resampling.nearest)
    print("Reprojected raster saved to:", output_file)
